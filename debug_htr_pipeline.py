import os
# pyrefly: ignore [missing-import]
import cv2
import json
import torch
import numpy as np
from PIL import Image
import torch.nn.functional as F
# pyrefly: ignore [missing-import]
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from spellchecker import SpellChecker


def deskew_image(gray_img: np.ndarray) -> np.ndarray:
    """Deskew gray image using minAreaRect on foreground contours."""
    blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    coords = np.column_stack(np.where(thresh > 0))
    if len(coords) == 0:
        return gray_img
    
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
        
    if abs(angle) < 0.5:
        return gray_img
        
    (h, w) = gray_img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(
        gray_img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
    )
    return rotated


def normalize_background(gray_img: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Remove uneven lighting/shadows using morphological background division
    and return normalized gray + binarized image.
    """
    # Estimate background illumination with large morphological dilation
    kernel_size = max(15, int(min(gray_img.shape[:2]) * 0.05))
    if kernel_size % 2 == 0:
        kernel_size += 1
    bg_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    background = cv2.morphologyEx(gray_img, cv2.MORPH_DILATE, bg_kernel)
    
    # Divide image by background to normalize lighting gradient
    normalized = cv2.divide(gray_img, background, scale=255)
    
    # Otsu thresholding on background-normalized image
    _, binarized = cv2.threshold(normalized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return normalized, binarized


def segment_lines(binarized_img: np.ndarray) -> list[tuple[int, int, int, int]]:
    """
    Segment text lines using resolution-independent morphological dilation.
    Returns list of bounding boxes (x, y, w, h).
    """
    h, w = binarized_img.shape[:2]
    
    # Resolution-independent dilation kernel
    kernel_w = max(15, int(w * 0.025))  # ~2.5% of width
    kernel_h = max(2, int(h * 0.005))   # ~0.5% of height
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_w, kernel_h))
    
    dilated = cv2.dilate(binarized_img, kernel, iterations=2)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    boxes = []
    min_area = (w * h) * 0.0001  # filter out tiny noise artifacts
    for cnt in contours:
        x, y, bw, bh = cv2.boundingRect(cnt)
        if bw * bh >= min_area and bh > 5:
            boxes.append((x, y, bw, bh))
            
    # Sort boxes top-to-bottom
    boxes = sorted(boxes, key=lambda b: b[1])
    return boxes


def pad_crop_for_trocr(crop: np.ndarray, target_aspect_ratio: float = 4.0) -> Image.Image:
    """
    Pads cropped image (especially isolated single letters or short words) 
    with white pixels to prevent visual distortion when resized by TrOCRProcessor.
    """
    h, w = crop.shape[:2]
    aspect_ratio = w / float(h)
    
    # If crop is too tall/square (e.g. single character like "A" or "K"), pad width
    desired_w = w
    desired_h = h
    if aspect_ratio < target_aspect_ratio:
        desired_w = int(h * target_aspect_ratio)
        
    # Add 20% margin padding around text
    margin_h = int(desired_h * 0.20)
    margin_w = int(desired_w * 0.15)
    
    pad_top = margin_h
    pad_bottom = margin_h
    pad_left = (desired_w - w) // 2 + margin_w
    pad_right = (desired_w - w) - (desired_w - w) // 2 + margin_w
    
    # Pad image with white background (255)
    if len(crop.shape) == 2:
        padded = cv2.copyMakeBorder(
            crop, pad_top, pad_bottom, pad_left, pad_right,
            cv2.BORDER_CONSTANT, value=255
        )
        pil_img = Image.fromarray(padded).convert("RGB")
    else:
        padded = cv2.copyMakeBorder(
            crop, pad_top, pad_bottom, pad_left, pad_right,
            cv2.BORDER_CONSTANT, value=(255, 255, 255)
        )
        pil_img = Image.fromarray(padded)
        
    return pil_img


def run_trocr_inference(
    model: VisionEncoderDecoderModel,
    processor: TrOCRProcessor,
    pil_img: Image.Image,
    device: str = "cpu"
) -> tuple[str, float, float, float]:
    """
    Runs TrOCR and computes token probabilities (min token prob and sequence mean prob).
    """
    pixel_values = processor(pil_img, return_tensors="pt").pixel_values.to(device)
    
    with torch.no_grad():
        outputs = model.generate(
            pixel_values,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=64,
            num_beams=4,
            early_stopping=True
        )
        
    raw_text = processor.decode(outputs.sequences[0], skip_special_tokens=True)
    
    # Token-level probability calculation
    scores = outputs.scores  # Tuple of step logit tensors
    gen_sequences = outputs.sequences[0]
    
    token_probs = []
    for idx, step_logits in enumerate(scores):
        prob_dist = F.softmax(step_logits[0], dim=-1)
        tok_id = gen_sequences[idx + 1]  # +1 to skip decoder_start_token
        tok_prob = prob_dist[tok_id].item()
        token_probs.append(tok_prob)
        
    if not token_probs:
        return raw_text, 0.0, 0.0, 0.0
        
    min_prob = min(token_probs)
    mean_prob = float(np.mean(token_probs))
    # Combined confidence score penalizes lines with any weak token
    line_confidence = mean_prob * min_prob
    
    return raw_text, min_prob, mean_prob, line_confidence


def safe_post_process(text: str, spell: SpellChecker) -> str:
    """
    Safe NLP correction:
    1. Only acts on Out-Of-Vocabulary (OOV) tokens.
    2. Applies glyph substitution candidates ONLY if candidate is a valid word.
    3. Prevents corruption of valid words (e.g. preserves 'turn', 'clock').
    """
    glyph_substitutions = {
        "rn": "m",
        "cl": "d",
        "vv": "w",
        "ii": "ll",
        "0": "O",
        "1": "l"
    }
    
    words = text.split()
    corrected_words = []
    
    for word in words:
        clean_word = "".join(c for c in word if c.isalnum())
        if not clean_word:
            corrected_words.append(word)
            continue
            
        # If word is valid dictionary word, digit, or short acronym, leave untouched
        if clean_word.lower() in spell or clean_word.isdigit() or len(clean_word) <= 1:
            corrected_words.append(word)
            continue
            
        # Try targeted glyph substitutions only for OOV word
        fixed_candidate = clean_word
        substituted = False
        for src, tgt in glyph_substitutions.items():
            if src in fixed_candidate:
                test_word = fixed_candidate.replace(src, tgt)
                if test_word.lower() in spell:
                    fixed_candidate = test_word
                    substituted = True
                    break
                    
        # If glyph sub didn't yield dictionary word, fall back to spellchecker correction
        if not substituted:
            suggestion = spell.correction(clean_word)
            if suggestion and len(suggestion) >= len(clean_word) - 1:
                fixed_candidate = suggestion
                
        corrected_word = word.replace(clean_word, fixed_candidate)
        corrected_words.append(corrected_word)
        
    return " ".join(corrected_words)


def main(image_path: str, output_dir: str = "debug_output"):
    os.makedirs(output_dir, exist_ok=True)
    crops_dir = os.path.join(output_dir, "crops")
    os.makedirs(crops_dir, exist_ok=True)
    
    print(f"[1/5] Loading image: {image_path}")
    orig_img = cv2.imread(image_path)
    if orig_img is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")
        
    gray = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
    
    print("[2/5] Running deskew & background normalization...")
    deskewed = deskew_image(gray)
    cv2.imwrite(os.path.join(output_dir, "01_deskewed.png"), deskewed)
    
    normalized, binarized = normalize_background(deskewed)
    cv2.imwrite(os.path.join(output_dir, "02_normalized.png"), normalized)
    cv2.imwrite(os.path.join(output_dir, "03_binarized.png"), binarized)
    
    print("[3/5] Segmenting lines with adaptive kernel...")
    boxes = segment_lines(binarized)
    
    viz_img = cv2.cvtColor(deskewed, cv2.COLOR_GRAY2BGR)
    for idx, (x, y, w, h) in enumerate(boxes):
        cv2.rectangle(viz_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(viz_img, f"#{idx}", (x, max(15, y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.imwrite(os.path.join(output_dir, "04_line_boxes.png"), viz_img)
    
    print(f"-> Detected {len(boxes)} line region(s).")
    
    print("[4/5] Initializing TrOCR model ('microsoft/trocr-base-handwritten')...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten").to(device)
    model.eval()
    
    spell = SpellChecker()
    
    results = []
    print("\n[5/5] Processing crops & evaluating confidence:")
    print("-" * 80)
    print(f"{'Crop':<6} | {'MinConf':<8} | {'MeanConf':<8} | {'Status':<10} | {'Raw TrOCR':<25} | {'Safe Corrected'}")
    print("-" * 80)
    
    for idx, (x, y, w, h) in enumerate(boxes):
        crop = deskewed[y:y+h, x:x+w]
        padded_pil = pad_crop_for_trocr(crop)
        
        # Save crop
        crop_filename = f"crop_{idx:03d}.png"
        padded_pil.save(os.path.join(crops_dir, crop_filename))
        
        raw_text, min_prob, mean_prob, line_conf = run_trocr_inference(
            model, processor, padded_pil, device=device
        )
        
        corrected_text = safe_post_process(raw_text, spell)
        is_flagged = line_conf < 0.55 or min_prob < 0.40
        status = "FLAGGED" if is_flagged else "OK"
        
        results.append({
            "crop_id": idx,
            "bbox": [x, y, w, h],
            "crop_path": os.path.join("crops", crop_filename),
            "raw_text": raw_text,
            "corrected_text": corrected_text,
            "min_token_prob": round(min_prob, 4),
            "mean_token_prob": round(mean_prob, 4),
            "line_confidence": round(line_conf, 4),
            "flagged_for_review": is_flagged
        })
        
        print(f"#{idx:<5} | {min_prob:<8.4f} | {mean_prob:<8.4f} | {status:<10} | {raw_text:<25} | {corrected_text}")

    # Save JSON summary report
    report_path = os.path.join(output_dir, "htr_debug_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print("-" * 80)
    print(f"\nDebug complete! Visuals and summary report saved to directory: '{output_dir}/'")


if __name__ == "__main__":
    import sys
    img_path = sys.argv[1] if len(sys.argv) > 1 else "sample.png"
    main(img_path)
