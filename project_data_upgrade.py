import os
import re
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
projects_path = os.path.join(BASE_DIR, 'js', 'projectsData.js')

with open(projects_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the array
array_match = re.search(r'const\s+PROJECTS_DATA\s*=\s*(\[.*\]);', content, re.DOTALL)
if array_match:
    try:
        # Since this is a JS file and not strict JSON (keys aren't quoted), we have to be careful.
        # But wait, parsing non-strict JSON in Python is hard.
        pass
    except Exception as e:
        pass
