import os
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
extensions = ['*.html', '*.md', '*.py', '*.json', '*.js', '*.ts', '*.tsx']

for ext in extensions:
    # use glob with recursive if needed, but in this case we can walk
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or 'node_modules' in root or '.venv' in root or '.next' in root:
            continue
        for file in files:
            if any(file.endswith(e[1:]) for e in extensions):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if 'sanjay-gl-b86631336' in content:
                        new_content = content.replace('sanjay-gl-b86631336', 'sanjay-gl-b86631336')
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated LinkedIn in {filepath}")
                except Exception as e:
                    pass
