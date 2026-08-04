import re
import json

with open(r"c:\Users\Sanjay G L\Desktop\portfiler\certificates.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract driveCerts entries
drive_matches = re.findall(r"driveId:\s*'([^']+)',\s*title:\s*([^,]+),\s*category:\s*(\[[^\]]+\])", content)

parsed_certs = []

# Named Awards
named_certs = [
    {"title": "PRAVIDHI — State Level BCA Tech Fest", "org": "JSS College for Women · SPARKTECHTHRA 2026", "cat": "Tech / Competitions", "date": "March 2026"},
    {"title": "National Road Safety Quiz", "org": "Ministry of Road Transport and Highways · MyGov", "cat": "Government", "date": "Verified"},
    {"title": "Online Quiz on Safe & Responsible Use of AI", "org": "MeitY · ISEA · CDAC · Digital India · MyGov", "cat": "Government / AI", "date": "Verified"},
    {"title": "Certificate of Completion — Web Dev Internship", "org": "Oasis Infobyte · AICTE OIB-SIP", "cat": "Internship", "date": "March 2026"},
    {"title": "Certificate of Appreciation — Star Performer", "org": "Oasis Infobyte · AICTE OIB-SIP", "cat": "Internship", "date": "March 2026"},
    {"title": "Python for Beginners", "org": "Verified Certificate", "cat": "Python / Tech", "date": "March 2026"}
]

for idx, (did, title_json, cat_str) in enumerate(drive_matches, 1):
    title = json.loads(title_json) if title_json.startswith('"') else title_json.strip("'")
    url = f"https://drive.google.com/file/d/{did}/view"
    parsed_certs.append({
        "index": idx,
        "title": title,
        "org": "Google Drive Verified Credential",
        "url": url,
        "driveId": did
    })

out_json = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\cert_summary_full.json"
with open(out_json, "w", encoding="utf-8") as f:
    json.dump({"named": named_certs, "drive": parsed_certs}, f, indent=2)

print(f"Dumped {len(named_certs)} named certs and {len(parsed_certs)} drive certs.")
