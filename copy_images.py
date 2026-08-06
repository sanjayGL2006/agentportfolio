import shutil
import os

src_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\ea4742f3-a212-4518-bdc1-0182b20c3bef"
dest_dir = r"c:\Users\Sanjay G L\Desktop\portfolio\assets"

files = {
    "accident_prediction_cover_1785944425341.png": "accident_prediction_cover.png",
    "sai_assistant_cover_1785944441312.png": "sai_assistant_cover.png"
}

for src_name, dest_name in files.items():
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        print(f"Copying {src_path} -> {dest_path}")
        shutil.copy2(src_path, dest_path)
    else:
        print(f"Error: {src_path} does not exist!")
