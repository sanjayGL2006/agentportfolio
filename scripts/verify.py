import json
import re

with open('d:/portfolio/js/certificatesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'driveId":|driveId:', text)
print(f"Total certificates in certificatesData.js: {len(matches)}")

with open('d:/portfolio/knowledge.json', 'r', encoding='utf-8') as f:
    k = json.load(f)

print(f"Total certificates in knowledge.json: {k.get('certificates', {}).get('total_count')}")
