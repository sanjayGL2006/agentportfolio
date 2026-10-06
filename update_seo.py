import os
import re
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read counts
try:
    with open(os.path.join(BASE_DIR, "js", "projectsData.js"), "r", encoding="utf-8") as f:
        projects_data = f.read()
        proj_count = len(re.findall(r'id:\s*\d+', projects_data))
        if proj_count == 0: proj_count = 69
except:
    proj_count = 69

try:
    with open(os.path.join(BASE_DIR, "js", "certificatesData.js"), "r", encoding="utf-8") as f:
        cert_data = f.read()
        cert_count = len(re.findall(r'id:\s*["\']', cert_data))
        if cert_count == 0: cert_count = 87
except:
    cert_count = 87

meta_desc = f"Sanjay G L (Sanju) – BCA student and Full Stack AI Developer in Shivamogga. {proj_count} projects, {cert_count} certificates, Python, React, AI."

pages = {
    "index.html": {
        "title": "Sanjay G L (Sanju) – Full Stack AI Developer, Shivamogga",
        "url": "/",
        "type": "website"
    },
    "projects.html": {
        "title": "Projects Showcase – Sanjay G L (Sanju)",
        "url": "/projects",
        "type": "website"
    },
    "certificates.html": {
        "title": "Certificates & Achievements – Sanjay G L (Sanju)",
        "url": "/certificates",
        "type": "website"
    },
    "privacy.html": {
        "title": "Privacy Policy – Sanjay G L",
        "url": "/privacy",
        "type": "website"
    }
}

json_ld_person = {
    "@context": "https://schema.org",
    "@type": ["Person", "ProfilePage"],
    "@id": "https://sanjaygl30ai.vercel.app/#person",
    "name": "Sanjay G L",
    "alternateName": ["Sanjay G. L.", "Sanju", "Sanjay GL"],
    "url": "https://sanjaygl30ai.vercel.app/",
    "image": "https://sanjaygl30ai.vercel.app/assets/profile.png",
    "jobTitle": "Full Stack AI Developer",
    "description": meta_desc,
    "alumniOf": {
        "@type": "CollegeOrUniversity",
        "name": "PES Institute of Advanced Management Studies"
    },
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Shivamogga",
        "addressRegion": "Karnataka",
        "addressCountry": "IN"
    },
    "knowsAbout": ["Python", "React", "AI", "Machine Learning", "Cybersecurity", "Full Stack Development"],
    "sameAs": [
        "https://github.com/sanjayGL2006",
        "https://www.linkedin.com/in/sanjay-gl-b86631336",
        "https://www.youtube.com/@spvm3techsolution",
        "https://www.instagram.com/spvm3techsolution",
        "https://t.me/Sanjaygl30"
    ]
}

def update_html_file(filename, config):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace Title
    content = re.sub(r'<title>.*?</title>', f'<title>{config["title"]}</title>', content, flags=re.IGNORECASE)
    
    # Replace Meta Description
    if '<meta name="description"' in content:
        content = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{meta_desc}">', content)
    else:
        content = content.replace('<head>', f'<head>\n  <meta name="description" content="{meta_desc}">')

    # Remove meta keywords
    content = re.sub(r'<meta name="keywords"[^>]*>\n?', '', content, flags=re.IGNORECASE)

    # Canonical
    full_url = f"https://sanjaygl30ai.vercel.app{config['url']}"
    if '<link rel="canonical"' in content:
        content = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{full_url}">', content)
    else:
        content = content.replace('<head>', f'<head>\n  <link rel="canonical" href="{full_url}">')

    # OG Tags
    content = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{config["title"]}">', content)
    content = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{full_url}">', content)
    content = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{meta_desc}">', content)

    # Clean internal URLs (.html -> clean)
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace("href='index.html'", "href='/'")
    content = content.replace('href="/index.html"', 'href="/"')
    content = content.replace('href="projects.html"', 'href="/projects"')
    content = content.replace('href="certificates.html"', 'href="/certificates"')
    content = content.replace('href="privacy.html"', 'href="/privacy"')

    # Replace JSON-LD
    json_ld_str = json.dumps(json_ld_person, indent=2)
    new_script = f'<script type="application/ld+json">\n{json_ld_str}\n  </script>'
    
    if '<script type="application/ld+json">' in content:
        content = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: new_script, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'{new_script}\n</head>')

    # Fix hidden SEO text on projects.html
    if filename == "projects.html":
        content = re.sub(r'<div[^>]*style="[^"]*display:\s*none[^"]*"[^>]*id="seo-content"[^>]*>.*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div class="sr-only"[^>]*>.*?</div>', '', content, flags=re.DOTALL)

    # Write back
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filename}")

for filename, config in pages.items():
    update_html_file(filename, config)

# Update sitemap.xml
sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://sanjaygl30ai.vercel.app/</loc>
        <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://sanjaygl30ai.vercel.app/projects</loc>
        <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://sanjaygl30ai.vercel.app/certificates</loc>
        <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://sanjaygl30ai.vercel.app/privacy</loc>
        <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.5</priority>
    </url>
</urlset>"""

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)
print("Updated sitemap.xml")
