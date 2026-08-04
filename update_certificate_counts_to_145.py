import re

# Update certificates.html
with open(r"c:\Users\Sanjay G L\Desktop\portfiler\certificates.html", "r", encoding="utf-8") as f:
    cert_content = f.read()

# Replace hardcoded counts
cert_content = re.sub(r'id="totalCount">\s*\d+\s*</div>', 'id="totalCount">145</div>', cert_content)
cert_content = re.sub(r'id="driveCount">\s*\d+\s*</div>', 'id="driveCount">139</div>', cert_content)
cert_content = re.sub(r'id="totalCertCount">\s*\d+\s*</span>', 'id="totalCertCount">145</span>', cert_content)
cert_content = re.sub(r'id="visibleCount">\s*\d+\s*</span>', 'id="visibleCount">145</span>', cert_content)
cert_content = re.sub(r'id="subTotalText">\s*\d+\s*certifications', 'id="subTotalText">145 certifications', cert_content)
cert_content = re.sub(r'<strong>\s*\d+\s*certifications and verified credentials</strong>', '<strong>145 certifications and verified credentials</strong>', cert_content)

# Make sure driveCerts slice or total count matches 139 Drive certs + 6 named certs = 145
with open(r"c:\Users\Sanjay G L\Desktop\portfiler\certificates.html", "w", encoding="utf-8") as f:
    f.write(cert_content)

print("Updated certificates.html to 145 total certificates!")

# Update index.html
with open(r"c:\Users\Sanjay G L\Desktop\portfiler\index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

idx_content = re.sub(r'(\d+)\+?\s*Certificates', '145+ Certificates', idx_content, flags=re.IGNORECASE)
idx_content = re.sub(r'data-count="(\d+)"([^>]*>.*?Certificates)', 'data-count="145"\\2', idx_content, flags=re.IGNORECASE)

with open(r"c:\Users\Sanjay G L\Desktop\portfiler\index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Updated index.html to 145+ Certificates!")
