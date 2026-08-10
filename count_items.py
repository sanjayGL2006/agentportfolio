import re, json

with open('js/projectsData.js', 'r', encoding='utf-8') as f:
    p_text = f.read()
    p_ids = re.findall(r'id:\s*[\d]+', p_text)
    print(f"Projects count in JS: {len(p_ids)}")

with open('js/certificatesData.js', 'r', encoding='utf-8') as f:
    c_text = f.read()
    named_ids = re.findall(r'id:\s*"cert-named-\d+"', c_text)
    drive_ids = re.findall(r'driveId:\s*\'', c_text)
    total_certs = len(named_ids) + len(drive_ids)
    print(f"Named Certs: {len(named_ids)}, Drive Certs: {len(drive_ids)}, Total Certs: {total_certs}")
