import re, os

base_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\616e388f-fdc3-433a-b63b-8f3b3d08b55f\scratch"

# Projects
p_text = open('js/projectsData.js', 'r', encoding='utf-8').read()
projects_raw = re.findall(r'title:\s*"([^"]+)",[\s\S]*?category:\s*"([^"]+)",[\s\S]*?tagline:\s*"([^"]+)"', p_text)

p_seo = ['<noscript>', '  <div class="seo-fallback" style="padding:20px;color:var(--text-muted)">', '    <h3>Full Projects Index for Search Engines</h3>', '    <ol>']
for title, category, tagline in projects_raw:
    p_seo.append(f'      <li><strong>{title}</strong> ({category}) — {tagline}</li>')
p_seo.extend(['    </ol>', '  </div>', '</noscript>'])

with open(os.path.join(base_dir, 'projects_seo_block.html'), 'w', encoding='utf-8') as f:
    f.write("\n".join(p_seo))

# Certificates
c_text = open('js/certificatesData.js', 'r', encoding='utf-8').read()
all_certs = re.findall(r'title:\s*"([^"]+)",\s*org:\s*"([^"]+)"', c_text)

c_seo = ['<noscript>', '  <div class="seo-fallback" style="padding:20px;color:var(--text-muted)">', '    <h3>Full Verified Certificates Index for Search Engines</h3>', '    <ol>']
for title, org in all_certs:
    c_seo.append(f'      <li><strong>{title}</strong> — {org}</li>')
c_seo.extend(['    </ol>', '  </div>', '</noscript>'])

with open(os.path.join(base_dir, 'certs_seo_block.html'), 'w', encoding='utf-8') as f:
    f.write("\n".join(c_seo))

print(f"Generated projects SEO block ({len(projects_raw)} items) and certs SEO block ({len(all_certs)} items)")
