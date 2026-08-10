import ast, re

def parse_js_array(filepath, var_name):
    content = open(filepath, 'r', encoding='utf-8').read()
    # Strip single line comments
    content = re.sub(r'//.*', '', content)
    match = re.search(r'const\s+' + var_name + r'\s*=\s*(\[[\s\S]*?\]);', content)
    if not match:
        return []
    raw = match.group(1)
    # Convert JS object key without quotes to string key
    python_str = re.sub(r'(?<=[{\s,])([a-zA-Z_]\w*)\s*:', r'"\1":', raw)
    # Convert JS true/false/null to Python True/False/None
    python_str = re.sub(r'\btrue\b', 'True', python_str)
    python_str = re.sub(r'\bfalse\b', 'False', python_str)
    python_str = re.sub(r'\bnull\b', 'None', python_str)
    return ast.literal_eval(python_str)

p = parse_js_array('js/projectsData.js', 'PROJECTS_DATA')
c = parse_js_array('js/certificatesData.js', 'CERTIFICATES_DATA')
print(f"AST Parsed Projects: {len(p)}")
print(f"AST Parsed Certificates: {len(c)}")
