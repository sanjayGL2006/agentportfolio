import shutil
import os

# Source artifact paths
source_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\ab366114-96ab-4bd4-bdb6-a3bc285b9768"
dest_dir = r"assets"

files_map = {
    "sindhanai_cover_1785984168965.png": "sindhanai_cover.png",
    "dermait_cover_1785984182729.png": "dermait_cover.png",
    "billing_cover_1785984197001.png": "billing_system_cover.png",
    "accident_prediction_cover_1785985056484.png": "accident_prediction_cover.png",
    "sai_assistant_cover_1785985071600.png": "sai_assistant_cover.png"
}

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    print(f"Created directory: {dest_dir}")

for src_name, dest_name in files_map.items():
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    
    if os.path.exists(src_path):
        try:
            shutil.copy2(src_path, dest_path)
            print(f"✓ Copied {src_name} -> {dest_path}")
        except Exception as e:
            print(f"✗ Error copying {src_name}: {e}")
    else:
        print(f"⚠ Warning: Source file does not exist: {src_path}")

print("\nAsset copy process completed!")
