import re
import json

with open(r"c:\Users\Sanjay G L\Desktop\portfiler\certificates.html", "r", encoding="utf-8") as f:
    content = f.read()

# Parse the driveCerts array from JS
match = re.search(r"let driveCerts = (\[[\s\S]*?\n\]);", content)

if match:
    # Read raw array string
    raw_array_str = match.group(1)
    
    # Parse individual JS objects using regex
    items = re.findall(r"\{\s*driveId:\s*'([^']+)',\s*title:\s*(\"[^\"]+\"|'[^']+'),\s*org:\s*(\"[^\"]+\"|'[^']+'),\s*category:\s*(\[[^\]]+\])\s*\}", raw_array_str)
    
    filtered_items = []
    for did, t_str, o_str, cat_str in items:
        t_clean = t_str.strip("\"'")
        # Filter out generic "Verified Credential #" or "Verified Certificate #"
        if not re.match(r"^Verified (Credential|Certificate) #\d+", t_clean, re.IGNORECASE):
            filtered_items.append((did, t_clean, o_str.strip("\"'"), cat_str))
            
    print(f"Filtered down from {len(items)} items to {len(filtered_items)} REAL certificates!")
    
    # Reconstruct driveCerts JS array
    new_js = "let driveCerts = [\n"
    for did, title, org, cat in filtered_items:
        new_js += f"  {{ driveId: '{did}', title: {json.dumps(title)}, org: {json.dumps(org)}, category: {cat} }},\n"
    new_js += "];"
    
    content = content.replace(match.group(0), new_js)

# Calculate totals: Named (6) + Filtered Drive (len(filtered_items))
total_count = 6 + len(filtered_items)
drive_count = len(filtered_items)

print(f"New Total Count: {total_count} (6 Named + {drive_count} Drive Docs)")

# Update HTML counters
content = re.sub(r'id="totalCount">\s*\d+\s*</div>', f'id="totalCount">{total_count}</div>', content)
content = re.sub(r'id="namedCount">\s*\d+\s*</div>', 'id="namedCount">6</div>', content)
content = re.sub(r'id="driveCount">\s*\d+\s*</div>', f'id="driveCount">{drive_count}</div>', content)
content = re.sub(r'id="visibleCount">\s*\d+\s*</span>', f'id="visibleCount">{total_count}</span>', content)
content = re.sub(r'id="totalCertCount">\s*\d+\s*</span>', f'id="totalCertCount">{total_count}</span>', content)
content = re.sub(r'id="subTotalText">\s*\d+\s*certifications', f'id="subTotalText">{total_count} certifications', content)

# Remove any driveCerts.slice override
content = content.replace("driveCerts = driveCerts.slice(0, 139);", "")

with open(r"c:\Users\Sanjay G L\Desktop\portfiler\certificates.html", "w", encoding="utf-8") as f:
    f.write(content)

# Update index.html
with open(r"c:\Users\Sanjay G L\Desktop\portfiler\index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

idx_content = re.sub(r'(\d+)\+?\s*Certificates', f'{total_count}+ Certificates', idx_content, flags=re.IGNORECASE)
idx_content = re.sub(r'Certificates \(\d+ Total\)', f'Certificates ({total_count} Total)', idx_content)

with open(r"c:\Users\Sanjay G L\Desktop\portfiler\index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)

print(f"Updated index.html to {total_count}+ Certificates!")
