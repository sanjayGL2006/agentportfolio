import json
import re

with open(r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\certificates_array.js", "r", encoding="utf-8") as f:
    certificates_js = f.read().strip()

def update_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace CERTIFICATES array using lambda to prevent re.sub escape issues
    pattern = r"const CERTIFICATES = \[\s*[\s\S]*?\n\];"
    if re.search(pattern, content):
        content = re.sub(pattern, lambda m: certificates_js, content)
        print(f"Updated CERTIFICATES array in {file_path}")
    else:
        print(f"WARNING: Could not find CERTIFICATES array pattern in {file_path}")

    # Update 70+ references to 90+ or 96
    content = content.replace("70+ verified certificates", "96 verified certificates")
    content = content.replace("70+ verified", "96 verified")
    content = content.replace("70+ <span", "96+ <span")
    content = content.replace('data-count="70"', 'data-count="96"')
    content = content.replace("70+ certificate archive", "96 certificate archive")

    # Update modal HTML if cert-modal exists
    old_modal_inner = '<button class="btn btn-outline" data-close-modal>Close Preview</button>'
    new_modal_inner = '''<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:16px">
      <a id="cert-modal-link" href="#" target="_blank" rel="noopener" class="btn btn-gold btn-sm"><i class="fa-solid fa-arrow-up-right-from-square"></i> View Certificate</a>
      <button class="btn btn-outline btn-sm" data-close-modal>Close</button>
    </div>'''
    if old_modal_inner in content:
        content = content.replace(old_modal_inner, new_modal_inner)
        print(f"Updated modal HTML in {file_path}")

    # Update modal JS listener
    old_modal_js = '''    modalIcon.innerHTML = `<i class="${c.icon}"></i>`;
    modalTitle.textContent = c.title.replace(/&amp;/g, '&');
    modalOrg.textContent = c.org.replace(/&amp;/g, '&');
    modalTag.textContent = c.cat;
    modal.classList.add('open');'''

    new_modal_js = '''    const modalLink = document.getElementById('cert-modal-link');
    modalIcon.innerHTML = `<i class="${c.icon}"></i>`;
    modalTitle.textContent = c.title.replace(/&amp;/g, '&');
    modalOrg.textContent = c.org.replace(/&amp;/g, '&');
    modalTag.textContent = c.cat;
    if (modalLink && c.url) {
      modalLink.href = c.url;
    }
    modal.classList.add('open');'''

    if old_modal_js in content:
        content = content.replace(old_modal_js, new_modal_js)
        print(f"Updated modal JS in {file_path}")

    # Update certCardHTML function
    old_card_body = '''    <div class="cert-body">
      <h4>${c.title}</h4>
      <span>${c.org}</span>
    </div>'''
    new_card_body = '''    <div class="cert-body">
      <h4>${c.title}</h4>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:8px">
        <span>${c.org}</span>
        <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:.78rem;color:var(--gold);opacity:.8"></i>
      </div>
    </div>'''
    if old_card_body in content:
        content = content.replace(old_card_body, new_card_body)
        print(f"Updated certCardHTML in {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

update_file(r"c:\Users\Sanjay G L\Desktop\portfiler\certificates.html")
update_file(r"c:\Users\Sanjay G L\Desktop\portfiler\index.html")
update_file(r"c:\Users\Sanjay G L\Desktop\portfiler\projects.html")
print("All files updated successfully.")
