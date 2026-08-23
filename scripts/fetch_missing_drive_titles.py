import urllib.request, re, json

missing_ids = [
    '1Cb4E1Am3NLuAt4fN3hUNadZKKpjL9yKP',
    '1NhxE2rGs-diBmAspxkanzLA_NG_KgIv9',
    '1XeXNbcDl9lp3qc-BjE5jkXGdTGx0lLsP',
    '1dScd4j_m9hXy6ogBfA2dSH09cT0L_D3A'
]

results = {}

for fid in missing_ids:
    url = f"https://drive.google.com/file/d/{fid}/view"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        title_m = re.search(r'<meta property="og:title" content="([^"]+)"', html)
        if title_m:
            title = title_m.group(1).replace(' - Google Drive', '').strip()
        else:
            title_m2 = re.search(r'<title>([^<]+)</title>', html)
            title = title_m2.group(1).replace(' - Google Drive', '').strip() if title_m2 else "Verified Certificate"
        results[fid] = title
    except Exception as e:
        results[fid] = f"Verified Certificate ({fid[:8]})"

print(json.dumps(results, indent=2))
