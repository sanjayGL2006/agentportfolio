import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\merged_certs.json", "r", encoding="utf-8") as f:
    records = json.load(f)

for r in records:
    txt = r.get("text", "").replace("\n", " ").strip()
    fn = r.get("filename", "")
    print(f"[{r['index']+1:02d}] FN: {fn}")
    if txt:
        print(f"     TXT: {txt[:250]}")
    else:
        print("     TXT: (No text extracted - image/scanned)")
