import re

with open('d:/portfolio/js/projectsData.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all live: "...", with live: null,
new_content = re.sub(r'live:\s*"[^"]*",', 'live: null,', content)

with open('d:/portfolio/js/projectsData.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated js/projectsData.js live links successfully!')
