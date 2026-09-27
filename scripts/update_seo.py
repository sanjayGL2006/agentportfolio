import re

seo_keywords = (
    "Sanjay, sanju, Sanjay G L, Sanjay G L bca student, Sanjay G L pes iams, "
    "Sanjay G L Full stack developer, Sanjay G L python developer, Sanjay G L Web developer, "
    "Sanjay G. L., BCA Student Shivamogga, PES IAMS Shivamogga, Full Stack Developer Shivamogga, "
    "Python Developer Karnataka, SPVM3 Tech Solution, Sanjay AIOS"
)

# 1. Update index.html
with open('d:/portfolio/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = re.sub(
    r'<meta name="keywords" content="[^"]*">',
    f'<meta name="keywords" content="{seo_keywords}">',
    idx_content
)

idx_content = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Sanjay G L (sanju) — Full Stack Developer, Python Developer, Web Developer & BCA Student at PES IAMS Shivamogga, Karnataka. Explore 62+ projects, 87+ certificates, and Sanjay AIOS co-pilot.">',
    idx_content
)

# Add alternateName in Schema.org JSON-LD
schema_replacement = '''    "name": "Sanjay G. L.",
    "alternateName": ["Sanjay", "sanju", "Sanjay G L", "Sanju G L", "Sanjay G L bca student", "Sanjay G L pes iams"],'''

idx_content = re.sub(r'"name":\s*"Sanjay G\. L\.",', schema_replacement, idx_content)

with open('d:/portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated index.html SEO meta tags & Schema.org JSON-LD!")

# 2. Update projects.html
with open('d:/portfolio/projects.html', 'r', encoding='utf-8') as f:
    proj_content = f.read()

proj_content = re.sub(
    r'<meta name="keywords" content="[^"]*">',
    f'<meta name="keywords" content="{seo_keywords}, Sanjay G L Projects, React Projects, Python Projects">',
    proj_content
)
proj_content = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Explore 62+ full stack web, AI, Python, and cybersecurity projects built by Sanjay G L (BCA Student at PES IAMS Shivamogga).">',
    proj_content
)
with open('d:/portfolio/projects.html', 'w', encoding='utf-8') as f:
    f.write(proj_content)
print("Updated projects.html SEO meta tags!")

# 3. Update certificates.html
with open('d:/portfolio/certificates.html', 'r', encoding='utf-8') as f:
    cert_content = f.read()

cert_content = re.sub(
    r'<meta name="keywords" content="[^"]*">',
    f'<meta name="keywords" content="{seo_keywords}, Sanjay G L Certificates, HackerRank, Microsoft Azure, NPTEL">',
    cert_content
)
cert_content = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Verified technical and academic certifications earned by Sanjay G L (sanju), BCA student at PES IAMS Shivamogga.">',
    cert_content
)
with open('d:/portfolio/certificates.html', 'w', encoding='utf-8') as f:
    f.write(cert_content)
print("Updated certificates.html SEO meta tags!")

# 4. Update privacy.html
with open('d:/portfolio/privacy.html', 'r', encoding='utf-8') as f:
    priv_content = f.read()

priv_content = re.sub(
    r'<meta name="keywords" content="[^"]*">',
    f'<meta name="keywords" content="{seo_keywords}">',
    priv_content
)
with open('d:/portfolio/privacy.html', 'w', encoding='utf-8') as f:
    f.write(priv_content)
print("Updated privacy.html SEO meta tags!")
