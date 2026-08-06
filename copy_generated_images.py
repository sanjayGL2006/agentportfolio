import os
import shutil

# Paths for the generated images in the brain artifacts directory
src_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\ea4742f3-a212-4518-bdc1-0182b20c3bef"
dest_dir = r"assets"

# Map generated filenames to final names
mapping = {
    "accident_prediction_cover_1785944425341.png": "accident_prediction_cover.png",
    "sai_assistant_cover_1785944441312.png": "sai_assistant_cover.png"
}

os.makedirs(dest_dir, exist_ok=True)

for src_name, dest_name in mapping.items():
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        print(f"Copying {src_path} -> {dest_path}")
        shutil.copy2(src_path, dest_path)
        print("Success!")
    else:
        print(f"Warning: Source file {src_path} not found.")
