import json, os

base_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\616e388f-fdc3-433a-b63b-8f3b3d08b55f\scratch"
json_path = os.path.join(base_dir, 'converted_drive_links.json')
out_path = os.path.join(base_dir, 'all_81_certificates_code_blocks.html')

if os.path.exists(json_path):
    data = json.load(open(json_path, 'r', encoding='utf-8'))
    
    html_lines = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>All 81 Certificates — HTML Code Blocks Export</title>",
        "  <style>",
        "    body { font-family: monospace; background: #0a0f1d; color: #e2e8f0; padding: 20px; }",
        "    .card { background: #1e293b; padding: 16px; margin-bottom: 20px; border-radius: 8px; border: 1px solid #334155; }",
        "    pre { background: #0f172a; padding: 12px; border-radius: 6px; overflow-x: auto; color: #34d399; }",
        "    h2 { color: #38bdf8; margin-top: 0; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>Sanjay G. L. — All 81 Google Drive Certificates HTML Code Blocks</h1>"
    ]
    
    for item in data:
        html_lines.append(f"  <div class='card'>")
        html_lines.append(f"    <h2>Certificate #{item['index']} (ID: {item['file_id']})</h2>")
        html_lines.append(f"    <h3>1. Direct Image Tag (img)</h3>")
        html_lines.append(f"    <pre>&lt;img src=\"{item['high_res_thumbnail_link']}\" alt=\"Certificate #{item['index']}\" loading=\"lazy\" style=\"width:100%; max-width:600px; border-radius:8px;\" /&gt;</pre>")
        html_lines.append(f"    <h3>2. Embeddable Preview (iframe)</h3>")
        html_lines.append(f"    <pre>&lt;iframe src=\"{item['embed_iframe_link']}\" width=\"100%\" height=\"500\" allow=\"autoplay\" style=\"border:none; border-radius:8px;\"&gt;&lt;/iframe&gt;</pre>")
        html_lines.append(f"    <h3>3. Direct View Link (a)</h3>")
        html_lines.append(f"    <pre>&lt;a href=\"{item['direct_view_link']}\" target=\"_blank\" rel=\"noopener\"&gt;View Full Resolution&lt;/a&gt;</pre>")
        html_lines.append(f"  </div>")
        
    html_lines.extend(["</body>", "</html>"])
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(html_lines))
        
    print(f"Generated HTML export file at {out_path} with {len(data)} certificate code block cards.")
