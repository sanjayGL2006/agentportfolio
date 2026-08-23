import re

files = [
    r"c:\Users\Sanjay G L\Desktop\portfiler\certificates.html",
    r"c:\Users\Sanjay G L\Desktop\portfiler\index.html",
    r"c:\Users\Sanjay G L\Desktop\portfiler\projects.html"
]

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add rel="noopener noreferrer" to any target="_blank" missing rel
    def fix_target_blank(match):
        full_tag = match.group(0)
        if "rel=" not in full_tag:
            return full_tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
        return full_tag

    new_content = re.sub(r'<a\s+[^>]*target="_blank"[^>]*>', fix_target_blank, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Updated rel='noopener noreferrer' on all external links across HTML files.")
