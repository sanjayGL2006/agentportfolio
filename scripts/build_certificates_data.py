import json
import os
import re

drive_results_path = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\drive_results.json"
extracted_certs_path = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\extracted_certs.json"

if not os.path.exists(extracted_certs_path):
    print("Extracted certs json not ready yet.")
    exit(0)

with open(drive_results_path, "r", encoding="utf-8") as f:
    drive_data = json.load(f)

with open(extracted_certs_path, "r", encoding="utf-8") as f:
    extracted_data = json.load(f)

merged = []
for i in range(len(drive_data)):
    d = drive_data[i]
    e = extracted_data[i] if i < len(extracted_data) else {}
    
    filename = d.get("filename", "")
    text = e.get("extracted_text", "")
    url = d.get("url", "")
    
    merged.append({
        "index": i,
        "filename": filename,
        "text": text,
        "url": url
    })

print(f"Merged {len(merged)} certificate records.")

out_merged = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\merged_certs.json"
with open(out_merged, "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=2)
