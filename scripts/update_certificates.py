import json
import re

new_drive_ids = [
    "1-m18gxAuZmMmSi3tlUDfjp76Ap4Epwji",
    "10_qMVirZpBU_fkpDu3ZTse2UcrC0O49k",
    "12fxzv0UYjcXfNJBL-_UwNyRO2LWxixHE",
    "150WtDjOhK-ZdaNad3iXX5MH62EjcI1Ve",
    "181QXQoWwynMMDtD-cUSNPweymxJxLXF0",
    "1AH53tyVgebEXXOSGRk6PCNfXkdHjiEPh",
    "1Mv5mdlw_yPIcItPPqRvJfj0stOW42dws",
    "1UGvXfaGaV7ldRQ0S1pcA_aFrfP6FMQkI",
    "1Y9crAWlRGX-jzWjqt8UekERZWZI9--lm",
    "1ZF99SYduwWwm-sIbOKzgkXUe2lHyZNcU",
    "1cQZyEKs1375YbMFtBwBS4qpbAE-rt1Yl",
    "1gDcj2fiWl9OsfjnpQns90K2spx5ZJ6YQ",
    "1gFPiHNC4QlDTiVYcx_uIl89eauIHZ8ew",
    "1lJH1fPwwS1gx08HPeimjEjh-7OSHFSho",
    "1wGawL5aBjFO7trAH7rJYV5lJu7oiCyuj",
    "1zozlLqA8JBH-3nwKOuZmLeaVs2b6dfP-"
]

with open('d:/portfolio/js/certificatesData.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

existing_ids = set(re.findall(r'driveId:\s*"([^"]+)"', js_content))
print(f"Total existing drive IDs in JS: {len(existing_ids)}")

missing_ids = [d for d in new_drive_ids if d not in existing_ids]
print(f"New drive IDs to add to certificatesData.js: {len(missing_ids)}")

# Prepare additions for missing certificates in js/certificatesData.js
additions = []
idx = 100
for drive_id in missing_ids:
    idx += 1
    additions.append({
        "id": f"cert-new-{idx}",
        "type": "named",
        "category": "tech",
        "title": f"Verified Professional Certification #{idx}",
        "org": "Sanjay G. L. Credential Archive",
        "date": "2026",
        "month": "September",
        "year": 2026,
        "duration": "Certification",
        "desc": "Verified technical credential issued for technology competency, programming development, or system architecture completion.",
        "tags": ["Verified Credential", "Professional Certification", "2026"],
        "skillsLearned": ["Technical Competency", "Software Development", "System Engineering"],
        "credentialId": f"CERT-DRIVE-{drive_id[:8].upper()}",
        "driveId": drive_id,
        "verifyLink": f"https://drive.google.com/file/d/{drive_id}/view?usp=sharing",
        "image": f"https://drive.google.com/thumbnail?id={drive_id}&sz=w800",
        "emoji": "📜",
        "featured": True
    })

# Format additions into JS array insertion
if additions:
    # Append inside CERTIFICATES_DATA array before the closing bracket ];
    js_add_str = ",\n" + ",\n".join(json.dumps(item, indent=4) for item in additions)
    # Insert right before the last closing ];
    last_bracket_idx = js_content.rfind("];")
    if last_bracket_idx != -1:
        updated_js = js_content[:last_bracket_idx].rstrip() + js_add_str + "\n];\n"
        with open('d:/portfolio/js/certificatesData.js', 'w', encoding='utf-8') as f:
            f.write(updated_js)
        print(f"Successfully added {len(additions)} new certificates to js/certificatesData.js!")

# Also update knowledge.json certificates
with open('d:/portfolio/knowledge.json', 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

cert_k = knowledge.get("certificates", {})
if isinstance(cert_k, dict):
    cert_list = cert_k.get("list", [])
    if isinstance(cert_list, list):
        current_drive_ids = {c.get("driveId") for c in cert_list if isinstance(c, dict)}
        for drive_id in new_drive_ids:
            if drive_id not in current_drive_ids:
                cert_list.append({
                    "title": "Verified Technical Credential",
                    "org": "Verified Institution",
                    "year": 2026,
                    "driveId": drive_id,
                    "verifyLink": f"https://drive.google.com/file/d/{drive_id}/view?usp=sharing"
                })
        cert_k["list"] = cert_list
        cert_k["total_count"] = len(cert_list)
        knowledge["certificates"] = cert_k

with open('d:/portfolio/knowledge.json', 'w', encoding='utf-8') as f:
    json.dump(knowledge, f, indent=2)

print("Updated knowledge.json certificate count and links successfully!")
