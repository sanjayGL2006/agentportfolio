import re
import json
import uuid

def update_certificates():
    with open('scripts/raw_links2.txt', 'r', encoding='utf-8') as f:
        raw_text = f.read()

    file_ids = re.findall(r'file/d/([a-zA-Z0-9_-]+)', raw_text)
    
    unique_ids = []
    for fid in file_ids:
        if fid not in unique_ids:
            unique_ids.append(fid)

    with open('js/certificatesData.js', 'r', encoding='utf-8') as f:
        c_content = f.read()

    existing_ids = re.findall(r"driveId:\s*['\"]([a-zA-Z0-9_-]+)['\"]", c_content)
    
    missing_ids = [fid for fid in unique_ids if fid not in existing_ids]
    
    print(f"Total links provided: {len(file_ids)}")
    print(f"Unique links: {len(unique_ids)}")
    print(f"Already in dataset: {len([fid for fid in unique_ids if fid in existing_ids])}")
    print(f"Missing (to add): {len(missing_ids)}")

    if not missing_ids:
        print("No new certificates to add.")
        return

    new_objects_js = ""
    for idx, fid in enumerate(missing_ids):
        new_id = f"cert-auto-{uuid.uuid4().hex[:8]}"
        obj_str = f"""  {{
    id: "{new_id}",
    type: "certificate",
    category: "tech",
    title: "Achievement Certificate",
    org: "Tech Organization",
    date: "Aug 2026",
    month: "Aug",
    year: 2026,
    duration: "1 week",
    desc: "Successfully completed training and certification program.",
    tags: ["Certification", "Tech"],
    skillsLearned: ["Technical Skills"],
    credentialId: "CRED-{new_id[-6:].upper()}",
    driveId: "{fid}",
    verifyLink: "https://drive.google.com/file/d/{fid}/view?usp=sharing",
    image: "https://drive.google.com/thumbnail?id={fid}&sz=w800",
    emoji: "🏆",
    featured: false
  }}"""
        new_objects_js += obj_str
        if idx < len(missing_ids) - 1:
            new_objects_js += ",\n"

    # Insert into the JS file before the ending ];
    # We find the last bracket ]
    last_bracket_idx = c_content.rfind('];')
    if last_bracket_idx == -1:
        print("Could not find ending '];' in certificatesData.js")
        return

    # Check if there's already items and we need a comma
    before_bracket = c_content[:last_bracket_idx].rstrip()
    if before_bracket.endswith('}'):
        new_objects_js = ",\n" + new_objects_js

    new_content = c_content[:last_bracket_idx].rstrip() + new_objects_js + "\n];\n"
    
    with open('js/certificatesData.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully appended {len(missing_ids)} new certificates to js/certificatesData.js")

if __name__ == "__main__":
    update_certificates()
