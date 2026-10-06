import os
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
html_files = glob.glob(os.path.join(BASE_DIR, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace target="_blank" without noreferrer
    content = content.replace('target="_blank" rel="noopener"', 'target="_blank" rel="noopener noreferrer"')
    content = content.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
    content = content.replace('rel="noopener noreferrer" rel="noopener noreferrer"', 'rel="noopener noreferrer"')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated rel attributes in {os.path.basename(filepath)}")
