import os

base_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\616e388f-fdc3-433a-b63b-8f3b3d08b55f\scratch"

p_seo = open(os.path.join(base_dir, 'projects_seo_block.html'), 'r', encoding='utf-8').read()
c_seo = open(os.path.join(base_dir, 'certs_seo_block.html'), 'r', encoding='utf-8').read()

# Update projects.html
with open('projects.html', 'r', encoding='utf-8') as f:
    p_html = f.read()

if '<noscript>' not in p_html:
    p_html = p_html.replace('<div class="projects-grid" id="projectsGrid"></div>', '<div class="projects-grid" id="projectsGrid"></div>\n\n      ' + p_seo)
    with open('projects.html', 'w', encoding='utf-8') as f:
        f.write(p_html)
    print("Inserted SEO block into projects.html")

# Update certificates.html
with open('certificates.html', 'r', encoding='utf-8') as f:
    c_html = f.read()

if '<noscript>' not in c_html:
    c_html = c_html.replace('<div class="certs-gallery-grid" id="certsGrid"></div>', '<div class="certs-gallery-grid" id="certsGrid"></div>\n\n      ' + c_seo)
    with open('certificates.html', 'w', encoding='utf-8') as f:
        f.write(c_html)
    print("Inserted SEO block into certificates.html")
