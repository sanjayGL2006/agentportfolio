import json
import re

with open(r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\certificates_array.js", "r", encoding="utf-8") as f:
    raw_js = f.read()

data_96 = json.loads(raw_js.replace("const CERTIFICATES = ", "").rstrip(";\n"))

user_drive_ids = [
  '101EnojK-vT0ofRpus24ChpMwcdWH-IZO',
  '130a-6aNkI7aFpkshYVmNix87aZ01UHcE',
  '14NdHcaMOp_PZazhdogWEivBFnuxQ48vH',
  '1594kubNx4SjWmslpFmbAXql2DA47uTtS',
  '16Qblc4p_4TJZaArfGaFd9mc6kNkqvBDi',
  '18UlXGYGdSoGRAr_Nc3K9ufm6YCDE5tkm',
  '1ADOYbQnbBXty6o5xvsXDtg6dNca1rupZ',
  '1DkSdN2bxFXmyph2ZH3dr86p-fYWwiDaY',
  '1G_Nus4dXaqf0VPqmshw1aGhlbMiGDaIH',
  '1HVb5L5YXxR38YU8lcw2VYG54gZD-uwvG',
  '1LsdDdH6e1HmUazBPOu3n6SBs-soR7RYo',
  '1R7EuPTZx7IZ7k-YZBWr7LAOL94O7dPaJ',
  '1RVRosZtbOqGHwrh3Kuui-e7CeYWdm4P8',
  '1RrSw1fQ3AnjW5GKWIry2lvtU1Npu146X',
  '1Rut3XME0UEtUBm2szqMxSuPTXE9rvQPt',
  '1Sv8HTIbdCxYf4pCpRsc4fNJ1CNty6HCp',
  '1Tb0rlxqkr8JJPmJpGWgWUvhq0Qi4Jqvs',
  '1YaNypcypvIUuyWW8z_YGPLDHxkUaqfbv',
  '1d4OsQE1h9Z6ygmzd2ljLgZi339CGvk3P',
  '1fb5eR4ho4Ca5Z4knefKxsqrwguU3kcQs',
  '1hKUXoYL5sBiNBJQS1waJsOfXeiBRR8ez',
  '1iT_5RwkR9liECzqi9BKVMNhEE4alRzSo',
  '1nTVsryCXykfBTOK6yeLXC-WOPbN4spGY',
  '1p4NrRfXAt_RJeyw4abjHGHSP_hVMEv-o',
  '1p7IJcaM_n72aonhS4kzXTE3c0pRMta_w',
  '1uMh0IOXelO4yaV4olwvCgusVXlGBjHmM',
  '1w89vGvXCAaSAOl_nbABD4q9isreEhRfY',
  '1xlMToEx0wICuj0DO0V-v5eVhdRG9rSMT',
  '10Vq4__te_q1wvywgIYY_4K0blPOavMx2',
  '10X0Dc2H73UQVjr4U-MVCDC85i2EsOPza',
  '12KVoyJXjFSlezR0KmmgPF8NI6PUjhsQm',
  '12kpcrCqwxr6pXerLfTx-qG2tUG5sL_Q_',
  '15fVZ-fG_TAJ3QtCnssQ78UevlX8F4VB7',
  '16MphtLGwY66nvg4jsP5xA7dXPv7IUrBp',
  '1877ISKlvZJQzSU4BifL2YmrxBv5bhjp5',
  '19slYtiNlnLEISoxdcVURfu8Bh-j5eZtw',
  '1ChT2M3eLGBeToJhNhR9oyPk5_FDB8-jJ',
  '1DFdXmKWOkln0TtwYCOCa--ScSguy0Ge6',
  '1DmLh4jeFLpJ-T2ZyjubCofobbuXcI2Gn',
  '1HxUJJoqbTEKHvs8MRoOu_Dohe-aPkaC8',
  '1IyBlb7kWZuM0dPXhye0XEB97VLqPj1kC',
  '1JgfgUFhCFIHQqosiw9H_f_IoarmSjGSR',
  '1K39PVSnV18lTUFvcog5qc_Vo7nk_D7tZ',
  '1Mnxz57JcjNMeW5j7SpMV4c0JOIrc6p3f',
  '1NqvIvqwazFLo19wHuO2PHnPQ3kw35JDK',
  '1OnGOESlfekUoEvZ56OzlXDhj9ru-QfmI',
  '1P21MYbYAFpijVCYDPFMcOxQbZpAjaHSg',
  '1Xh1NYTGBxVToxpLS5ngiHu6yyR4c7IBI',
  '1Xto3xt5RG2EptLCsuap4brTlRGyiw7gG',
  '1_CYRjPS0KAtxVsVmE_Jl-IltmF6l_VkF',
  '1abdQquiBZSFFWkD1l8k9Rzdrv-1Xnlw5',
  '1b0GV6XlyExJ1Fd0qkuATHeqt887cq4Sa',
  '1fETmYIeOCcBhFnTrrZh4GXZ9Q3mRejdX',
  '1ipYVxar9n7a1ayOeLVQExL1wF9Q5vNqv',
  '1n1cflo3Fg-MyWNkX1eqkQzV6ru4m5Fzg',
  '1oqPDg7U2enLUcCaLuygE7UM6XFqfhvV7',
  '1pE1c-P_VrxYxO72VrMEDH_cCfADTpZ9U',
  '1pLglzX_GC-OhFCoDOK9lEE_-9jbVgIHs',
  '1pf2zSgxW7_OZfcxEsB6wkM_61o2M-Ddp',
  '1sfJv-CTGomeDyZR39of7kU8Qxnhwj0RK',
  '1stEhxu3MUiTfByiaMhe5qYFr-n8BG1EB',
  '1sxOO59k6UwVmHVQfRzVGoD20bj32EvDE',
  '1wkRqKU2HE98FeycskozqgXk40i1fF7hl',
  '1zXArkZNUWyfe9Quz0k6lhWVCcN5rA4rH',
  '1GbYj1y9ao2wGQeXyrp5cTjt4zszK61iM',
  '1PzYpEBBYJvfsExPJy9ksPS4oR88PaTDy',
  '1i-CTvb4kMtdGe7nWxSMxEwKUPssghrhT',
  '1pu_99X1w68I98YhkZIAd8YaeVVuFcWSz',
  '1x0y_iFE7NBF0TUe03u9FHksX1AjA9SmJ'
]

drive_entries = []
seen_ids = set()

for idx, did in enumerate(user_drive_ids):
    if did not in seen_ids:
        seen_ids.add(did)
        drive_entries.append({
            "driveId": did,
            "title": f"Verified Certificate #{len(drive_entries)+1}",
            "cat": ["drive", "tech"]
        })

for item in data_96:
    url = item.get("url", "")
    match = re.search(r'/d/([^/]+)', url)
    if match:
        did = match.group(1)
        if did not in seen_ids:
            seen_ids.add(did)
            cat_list = ["drive"]
            c_cat = item.get("cat", "")
            if c_cat == "government":
                cat_list.append("government")
            elif c_cat == "internships":
                cat_list.append("internship")
            else:
                cat_list.append("tech")

            drive_entries.append({
                "driveId": did,
                "title": item.get("title", f"Verified Certificate #{len(drive_entries)+1}"),
                "cat": cat_list
            })

drive_certs_js = "let driveCerts = [\n"
for d in drive_entries:
    cats_str = json.dumps(d['cat'])
    drive_certs_js += f"  {{ driveId: '{d['driveId']}', title: {json.dumps(d['title'])}, category: {cats_str} }},\n"
drive_certs_js += "];\n"

# Full HTML template
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Certificates &amp; Credentials — Sanjay GL</title>
<meta name="description" content="All certificates and credentials earned by Sanjay GL — BCA student, developer, and NSS volunteer from Shivamogga, Karnataka."/>
<link rel="icon" type="image/svg+xml" href="assets/logo.svg">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&amp;family=Space+Mono:wght@400;700&amp;family=DM+Sans:ital,wght@0,300;0,400;0,500;1,400&amp;display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#070b14;--surface:#0d1424;--surface2:#131d30;
  --border:rgba(100,210,255,0.12);--accent:#38d9f5;
  --accent2:#f5c038;--accent3:#56f5a0;--text:#e8f0ff;
  --muted:#7a8aaa;--glow:0 0 40px rgba(56,217,245,0.18);
}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;overflow-x:hidden;}}

/* ── NAV ── */
nav{{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:16px 60px;background:rgba(7,11,20,0.95);backdrop-filter:blur(18px);border-bottom:1px solid var(--border);}}
.nav-logo{{display:flex;align-items:center;gap:12px;text-decoration:none;}}
.nav-brand{{font-family:'Syne',sans-serif;font-size:1.12rem;font-weight:800;color:var(--text);letter-spacing:0.04em;}}
.nav-brand span{{color:var(--accent);}}
.nav-back{{display:inline-flex;align-items:center;gap:8px;font-family:'Space Mono',monospace;font-size:0.72rem;color:var(--muted);text-decoration:none;letter-spacing:0.08em;text-transform:uppercase;transition:color 0.2s;border:1px solid var(--border);padding:8px 16px;border-radius:8px;}}
.nav-back:hover{{color:var(--accent);border-color:rgba(56,217,245,0.4);}}
.nav-back svg{{transition:transform 0.2s;}}
.nav-back:hover svg{{transform:translateX(-3px);}}

/* ── HERO BANNER ── */
.cert-hero{{position:relative;padding:130px 60px 70px;overflow:hidden;border-bottom:1px solid var(--border);}}
.cert-hero-orb{{position:absolute;border-radius:50%;filter:blur(80px);pointer-events:none;}}
.cert-hero-orb-1{{width:600px;height:600px;background:radial-gradient(circle,rgba(56,217,245,0.07),transparent 70%);top:-200px;right:-100px;}}
.cert-hero-orb-2{{width:400px;height:400px;background:radial-gradient(circle,rgba(245,192,56,0.05),transparent 70%);bottom:-100px;left:-80px;}}
.cert-hero-inner{{max-width:1100px;margin:0 auto;position:relative;z-index:1;}}
.cert-hero-label{{display:inline-flex;align-items:center;gap:8px;background:rgba(56,217,245,0.08);border:1px solid rgba(56,217,245,0.25);border-radius:100px;padding:6px 18px;font-family:'Space Mono',monospace;font-size:0.72rem;color:var(--accent);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:20px;}}
.cert-hero-label::before{{content:'';width:7px;height:7px;border-radius:50%;background:var(--accent3);animation:pulse 2s infinite;}}
@keyframes pulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:0.3;transform:scale(0.8)}}}}
.cert-hero h1{{font-family:'Syne',sans-serif;font-size:clamp(2.2rem,5vw,4rem);font-weight:800;line-height:1.1;letter-spacing:-0.02em;margin-bottom:18px;}}
.cert-hero h1 span{{color:var(--accent);}}
.cert-hero-sub{{font-size:1rem;color:var(--muted);line-height:1.75;max-width:620px;margin-bottom:30px;}}
.cert-hero-sub strong{{color:var(--text);}}
.cert-stats{{display:flex;gap:30px;flex-wrap:wrap;margin-top:10px;}}
.cert-stat{{text-align:left;}}
.cert-stat-num{{font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:var(--accent);}}
.cert-stat-label{{font-family:'Space Mono',monospace;font-size:0.68rem;color:var(--muted);letter-spacing:0.08em;text-transform:uppercase;margin-top:2px;}}

/* ── PROFILE CARD ── */
.profile-band{{background:var(--surface);border-bottom:1px solid var(--border);padding:30px 60px;}}
.profile-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;gap:28px;flex-wrap:wrap;}}
.profile-avatar{{width:72px;height:72px;border-radius:50%;object-fit:cover;border:2px solid rgba(245,192,56,0.5);box-shadow:0 0 20px rgba(245,192,56,0.2);flex-shrink:0;}}
.profile-details{{flex:1;}}
.profile-name{{font-family:'Syne',sans-serif;font-size:1.25rem;font-weight:800;}}
.profile-title{{font-size:0.86rem;color:var(--muted);margin-top:3px;line-height:1.5;}}
.profile-chips{{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;}}
.profile-chip{{font-family:'Space Mono',monospace;font-size:0.66rem;padding:4px 12px;border-radius:6px;border:1px solid var(--border);color:var(--muted);background:var(--surface2);}}
.profile-chip.hi{{border-color:rgba(56,217,245,0.3);color:var(--accent);background:rgba(56,217,245,0.06);}}
.profile-chip a{{color:inherit;text-decoration:none;}}
.profile-chip a:hover{{color:var(--accent);}}
.profile-links{{display:flex;gap:10px;margin-left:auto;flex-wrap:wrap;}}
.profile-link{{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;border-radius:8px;font-family:'Space Mono',monospace;font-size:0.68rem;text-decoration:none;transition:transform 0.2s,box-shadow 0.2s;letter-spacing:0.04em;}}
.profile-link-primary{{background:var(--accent);color:var(--bg);font-weight:700;}}
.profile-link-primary:hover{{transform:translateY(-2px);box-shadow:0 6px 22px rgba(56,217,245,0.35);}}
.profile-link-outline{{border:1px solid var(--border);color:var(--muted);}}
.profile-link-outline:hover{{border-color:rgba(56,217,245,0.35);color:var(--accent);transform:translateY(-2px);}}

/* ── FILTER BAR ── */
.filter-bar{{position:sticky;top:73px;z-index:50;background:rgba(7,11,20,0.96);backdrop-filter:blur(16px);border-bottom:1px solid var(--border);padding:16px 60px;}}
.filter-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;gap:12px;flex-wrap:wrap;}}
.filter-label{{font-family:'Space Mono',monospace;font-size:0.65rem;color:var(--muted);letter-spacing:0.1em;text-transform:uppercase;white-space:nowrap;}}
.filter-btn{{font-family:'Space Mono',monospace;font-size:0.68rem;padding:6px 14px;border-radius:100px;border:1px solid var(--border);color:var(--muted);background:transparent;cursor:pointer;transition:all 0.2s;letter-spacing:0.04em;white-space:nowrap;}}
.filter-btn:hover{{border-color:rgba(56,217,245,0.35);color:var(--accent);}}
.filter-btn.active{{background:var(--accent);border-color:var(--accent);color:var(--bg);font-weight:700;}}
.search-box{{margin-left:auto;display:flex;align-items:center;gap:8px;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:7px 14px;transition:border-color 0.2s;}}
.search-box:focus-within{{border-color:rgba(56,217,245,0.4);}}
.search-box svg{{color:var(--muted);flex-shrink:0;}}
.search-box input{{background:transparent;border:none;outline:none;font-family:'DM Sans',sans-serif;font-size:0.88rem;color:var(--text);width:180px;}}
.search-box input::placeholder{{color:var(--muted);opacity:0.6;}}

/* ── MAIN GRID ── */
.certs-main{{max-width:1100px;margin:0 auto;padding:50px 60px 90px;}}
.certs-count{{font-family:'Space Mono',monospace;font-size:0.7rem;color:var(--muted);letter-spacing:0.08em;margin-bottom:28px;}}
.certs-count span{{color:var(--accent);}}
.certs-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:22px;}}
.no-results{{text-align:center;padding:80px 20px;color:var(--muted);}}
.no-results-icon{{font-size:3rem;margin-bottom:16px;}}
.no-results-text{{font-family:'Syne',sans-serif;font-size:1.1rem;font-weight:700;color:var(--text);margin-bottom:8px;}}
.no-results-sub{{font-size:0.88rem;}}

/* ── CERT CARD ── */
.cert-card{{background:var(--surface);border:1px solid var(--border);border-radius:18px;overflow:hidden;cursor:pointer;transition:transform 0.25s,border-color 0.25s,box-shadow 0.25s;display:flex;flex-direction:column;position:relative;}}
.cert-card:hover{{transform:translateY(-6px);border-color:rgba(56,217,245,0.4);box-shadow:0 16px 40px rgba(56,217,245,0.12);}}
.cert-thumb{{width:100%;height:150px;overflow:hidden;position:relative;background:var(--surface2);}}
.cert-thumb img{{width:100%;height:100%;object-fit:cover;object-position:top;transition:transform 0.4s;}}
.cert-card:hover .cert-thumb img{{transform:scale(1.04);}}
.cert-thumb-overlay{{position:absolute;inset:0;background:linear-gradient(to bottom,transparent 50%,rgba(13,20,36,0.8));}}
.cert-thumb-fallback{{width:100%;height:100%;display:none;align-items:center;justify-content:center;font-size:2.8rem;background:linear-gradient(135deg,var(--surface),rgba(56,217,245,0.06));}}
.cert-type-badge{{position:absolute;top:10px;right:10px;font-family:'Space Mono',monospace;font-size:0.6rem;padding:3px 9px;border-radius:100px;letter-spacing:0.05em;z-index:2;}}
.badge-named{{background:rgba(86,245,160,0.15);border:1px solid rgba(86,245,160,0.35);color:#56f5a0;}}
.badge-drive{{background:rgba(56,217,245,0.12);border:1px solid rgba(56,217,245,0.3);color:var(--accent);}}
.cert-body{{padding:18px 20px;flex:1;display:flex;flex-direction:column;gap:8px;}}
.cert-issuer{{font-size:0.7rem;color:var(--muted);font-family:'Space Mono',monospace;letter-spacing:0.03em;}}
.cert-name{{font-family:'Syne',sans-serif;font-weight:700;font-size:0.95rem;line-height:1.35;color:var(--text);}}
.cert-date{{font-size:0.7rem;color:var(--accent);font-family:'Space Mono',monospace;}}
.cert-desc{{font-size:0.82rem;color:var(--muted);line-height:1.65;flex:1;}}
.cert-tags{{display:flex;flex-wrap:wrap;gap:5px;margin-top:4px;}}
.cert-tag{{font-family:'Space Mono',monospace;font-size:0.6rem;padding:2px 8px;border-radius:4px;background:rgba(56,217,245,0.06);border:1px solid rgba(56,217,245,0.15);color:var(--muted);}}
.cert-footer{{padding:14px 20px;border-top:1px solid var(--border);display:flex;align-items:center;gap:10px;}}
.cert-view-btn{{display:inline-flex;align-items:center;gap:6px;background:var(--accent);color:var(--bg);padding:8px 16px;border-radius:7px;font-family:'Space Mono',monospace;font-size:0.68rem;font-weight:700;border:none;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;text-decoration:none;}}
.cert-view-btn:hover{{transform:translateY(-1px);box-shadow:0 6px 20px rgba(56,217,245,0.35);}}
.cert-open-link{{display:inline-flex;align-items:center;gap:5px;font-family:'Space Mono',monospace;font-size:0.65rem;color:var(--muted);text-decoration:none;padding:8px 12px;border:1px solid var(--border);border-radius:7px;transition:color 0.2s,border-color 0.2s;}}
.cert-open-link:hover{{color:var(--accent);border-color:rgba(56,217,245,0.3);}}

/* ── MODAL ── */
.modal-overlay{{position:fixed;inset:0;z-index:1000;background:rgba(7,11,20,0.96);backdrop-filter:blur(16px);display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity 0.3s;padding:20px;}}
.modal-overlay.active{{opacity:1;pointer-events:all;}}
.modal-box{{background:var(--surface);border:1px solid var(--border);border-radius:24px;padding:0;max-width:740px;width:100%;max-height:92vh;overflow-y:auto;position:relative;transform:scale(0.94) translateY(22px);transition:transform 0.3s;box-shadow:0 30px 80px rgba(0,0,0,0.7);}}
.modal-overlay.active .modal-box{{transform:scale(1) translateY(0);}}
.modal-close{{position:absolute;top:16px;right:16px;background:var(--surface2);border:1px solid var(--border);border-radius:50%;width:38px;height:38px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--muted);font-size:1rem;transition:color 0.2s,border-color 0.2s;z-index:2;}}
.modal-close:hover{{color:#ff6b6b;border-color:rgba(255,100,100,0.3);}}
.modal-body{{padding:28px 32px;}}
.modal-badge{{display:inline-flex;align-items:center;gap:6px;font-family:'Space Mono',monospace;font-size:0.66rem;padding:4px 12px;border-radius:100px;margin-bottom:14px;}}
.modal-title{{font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:800;line-height:1.2;margin-bottom:8px;}}
.modal-org{{font-size:0.88rem;color:var(--accent);font-family:'Space Mono',monospace;margin-bottom:18px;}}
.modal-desc{{font-size:0.93rem;color:var(--muted);line-height:1.78;margin-bottom:22px;}}
.modal-meta{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px;}}
.meta-chip{{padding:5px 12px;border-radius:7px;background:rgba(56,217,245,0.07);border:1px solid rgba(56,217,245,0.2);font-family:'Space Mono',monospace;font-size:0.68rem;color:var(--accent);}}
.modal-actions{{display:flex;gap:10px;flex-wrap:wrap;}}
.modal-btn-primary{{display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:10px;background:var(--accent);color:var(--bg);font-family:'Syne',sans-serif;font-weight:700;font-size:0.9rem;text-decoration:none;transition:transform 0.2s,box-shadow 0.2s;border:none;cursor:pointer;}}
.modal-btn-primary:hover{{transform:translateY(-2px);box-shadow:0 8px 28px rgba(56,217,245,0.4);}}
.modal-btn-outline{{display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:10px;background:transparent;color:var(--text);font-family:'Syne',sans-serif;font-weight:700;font-size:0.9rem;text-decoration:none;border:1px solid var(--border);transition:border-color 0.2s,color 0.2s,transform 0.2s;}}
.modal-btn-outline:hover{{border-color:rgba(56,217,245,0.35);color:var(--accent);transform:translateY(-2px);}}
.modal-drive-frame{{border-radius:14px;overflow:hidden;border:1px solid var(--border);background:var(--surface2);margin-bottom:20px;}}
.modal-drive-frame iframe{{display:block;border:none;width:100%;height:500px;}}
.modal-drive-bar{{padding:12px 18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;}}
.modal-drive-label{{font-family:'Space Mono',monospace;font-size:0.7rem;color:var(--muted);}}

/* ── FOOTER ── */
footer{{text-align:center;padding:30px 60px;border-top:1px solid var(--border);font-family:'Space Mono',monospace;font-size:0.7rem;color:var(--muted);background:var(--surface);}}
footer span{{color:var(--accent);}}
footer a{{color:var(--muted);text-decoration:none;transition:color 0.2s;}}
footer a:hover{{color:var(--accent);}}

/* ── RESPONSIVE ── */
@media(max-width:768px){{
  nav{{padding:14px 24px;}}
  .cert-hero{{padding:100px 24px 50px;}}
  .profile-band{{padding:22px 24px;}}
  .profile-links{{margin-left:0;width:100%;}}
  .filter-bar{{padding:14px 24px;}}
  .certs-main{{padding:36px 24px 60px;}}
  .modal-body{{padding:22px 22px;}}
  .search-box input{{width:120px;}}
}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(24px)}}to{{opacity:1;transform:translateY(0)}}}}
.fadein{{animation:fadeUp 0.6s ease both;}}
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <a href="index.html" class="nav-logo">
    <img src="assets/logo.svg" alt="Sanjay GL" style="width:40px;height:40px;border-radius:50%;object-fit:cover;border:2px solid rgba(245,192,56,0.5);box-shadow:0 0 12px rgba(245,192,56,0.2);" onerror="this.onerror=null;this.src='assets/logo.svg';">
    <div class="nav-brand">Sanjay <span>GL</span></div>
  </a>
  <a href="index.html" class="nav-back">
    <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
    Back to Portfolio
  </a>
</nav>

<!-- HERO BANNER -->
<div class="cert-hero">
  <div class="cert-hero-orb cert-hero-orb-1"></div>
  <div class="cert-hero-orb cert-hero-orb-2"></div>
  <div class="cert-hero-inner fadein">
    <div class="cert-hero-label">04 — Achievements</div>
    <h1>Certificates &amp; <span>Credentials</span></h1>
    <p class="cert-hero-sub">
      A complete record of <strong id="subTotalText">{len(drive_entries)+6} certifications and verified credentials</strong> earned by <strong>Sanjay GL</strong> — BCA student, developer, and NSS volunteer from Shivamogga, Karnataka, India.
    </p>
    <div class="cert-stats">
      <div class="cert-stat">
        <div class="cert-stat-num" id="totalCount">{len(drive_entries)+6}</div>
        <div class="cert-stat-label">Total Certificates</div>
      </div>
      <div class="cert-stat">
        <div class="cert-stat-num" id="namedCount">6</div>
        <div class="cert-stat-label">Named Awards</div>
      </div>
      <div class="cert-stat">
        <div class="cert-stat-num" id="driveCount">{len(drive_entries)}</div>
        <div class="cert-stat-label">Verified Documents</div>
      </div>
      <div class="cert-stat">
        <div class="cert-stat-num">2026</div>
        <div class="cert-stat-label">Latest Year</div>
      </div>
    </div>
  </div>
</div>

<!-- PROFILE CARD -->
<div class="profile-band">
  <div class="profile-inner">
    <img src="sanju.jpg" alt="Sanjay GL" class="profile-avatar" onerror="this.onerror=null;this.src='assets/logo.svg';">
    <div class="profile-details">
      <div class="profile-name">Sanjay GL</div>
      <div class="profile-title">BCA Student · PES Institute of Advanced Management Studies, Shivamogga · 2nd Year, 4th Semester</div>
      <div class="profile-chips">
        <span class="profile-chip hi">Full-Stack Aspirant</span>
        <span class="profile-chip hi">AI Workflow Engineer</span>
        <span class="profile-chip">NSS Volunteer</span>
        <span class="profile-chip">Shivamogga, Karnataka, India</span>
        <span class="profile-chip"><a href="mailto:sanjaygl2006@gmail.com">sanjaygl2006@gmail.com</a></span>
        <span class="profile-chip">+91 81239 81877</span>
      </div>
    </div>
    <div class="profile-links">
      <a href="https://www.linkedin.com/in/sanjay-gl-b86631336/" target="_blank" rel="noopener noreferrer" class="profile-link profile-link-primary">
        <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        LinkedIn
      </a>
      <a href="https://github.com/sanjayGL2006" target="_blank" rel="noopener noreferrer" class="profile-link profile-link-outline">
        <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
        GitHub
      </a>
      <a href="index.html" class="profile-link profile-link-outline">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
        Portfolio
      </a>
      <a href="https://www.facebook.com/people/Sanjay-G-L-Sanju/100084034332588/" target="_blank" rel="noopener noreferrer" class="profile-link profile-link-outline">
        <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
        Facebook
      </a>
    </div>
  </div>
</div>

<!-- FILTER BAR -->
<div class="filter-bar">
  <div class="filter-inner">
    <span class="filter-label">Filter:</span>
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="named">Named Awards</button>
    <button class="filter-btn" data-filter="drive">Verified Docs</button>
    <button class="filter-btn" data-filter="internship">Internship</button>
    <button class="filter-btn" data-filter="government">Government</button>
    <button class="filter-btn" data-filter="tech">Tech / Coding</button>
    <div class="search-box">
      <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" id="searchInput" placeholder="Search certificates..." autocomplete="off">
    </div>
  </div>
</div>

<!-- DOWNLOAD RESUME SECTION -->
<div style="background:var(--surface);border-bottom:1px solid var(--border);padding:28px 60px;">
  <div style="max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:20px;">
    <div>
      <h3 style="font-family:'Syne',sans-serif;font-weight:700;font-size:1.15rem;color:var(--text);margin-bottom:6px;">📄 Get My Full Resume</h3>
      <p style="font-size:0.88rem;color:var(--muted);">Download my comprehensive resume with all experience, skills, education, and achievements in a clean DOCX format.</p>
    </div>
    <a class="resume-print-btn" href="Sanjay_GL_Resume.docx" download style="display:inline-flex;align-items:center;gap:8px;padding:12px 28px;border-radius:10px;background:var(--accent);color:var(--bg);font-family:'Syne',sans-serif;font-weight:700;font-size:0.95rem;text-decoration:none;transition:transform 0.2s,box-shadow 0.2s;border:none;cursor:pointer;white-space:nowrap;">
      <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
      Download Resume (DOCX)
    </a>
  </div>
</div>

<!-- MAIN GRID -->
<div class="certs-main">
  <div class="certs-count">Showing <span id="visibleCount">{len(drive_entries)+6}</span> of <span id="totalCertCount">{len(drive_entries)+6}</span> certificates</div>
  <div class="certs-grid" id="certsGrid"></div>
  <div class="no-results" id="noResults" style="display:none;">
    <div class="no-results-icon">🔍</div>
    <div class="no-results-text">No certificates found</div>
    <div class="no-results-sub">Try a different search term or filter</div>
  </div>
</div>

<!-- MODAL -->
<div class="modal-overlay" id="modalOverlay" onclick="closeModal(event)">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal()">✕</button>
    <div id="modalContent"></div>
  </div>
</div>

<footer>
  <p>Sanjay GL · BCA Student · PES IAMS, Shivamogga · <span>Karnataka, India</span> · <a href="mailto:sanjaygl2006@gmail.com">sanjaygl2006@gmail.com</a> · <a href="index.html">← Back to Portfolio</a></p>
</footer>

<script>
// ── ALL CERTIFICATE DATA ──
const namedCerts = [
  {{
    type: 'named',
    category: ['tech','named'],
    title: 'PRAVIDHI — State Level BCA Tech Fest',
    org: 'JSS College for Women · SPARKTECHTHRA 2026',
    date: '4 & 5 March 2026',
    desc: 'Participated in the Coding event at the State Level BCA Tech Fest SPARKTECHTHRA 2026 held at JSS College for Women, Mysore. Competed among talented student developers from across Karnataka in a high-intensity coding challenge.',
    tags: ['State Level', 'Coding', 'BCA Tech Fest', '2026', 'Mysore'],
    emoji: '🏆'
  }},
  {{
    type: 'named',
    category: ['government','named'],
    title: 'National Road Safety Quiz',
    org: 'Ministry of Road Transport and Highways · MyGov',
    date: 'Certificate of Participation',
    desc: 'Participated in the National Road Safety Quiz organised by the Ministry of Road Transport and Highways, Government of India through MyGov platform. Demonstrated awareness of road safety rules and regulations.',
    tags: ['Government of India', 'Road Safety', 'MyGov', 'Quiz', 'Ministry'],
    emoji: '🛡️'
  }},
  {{
    type: 'named',
    category: ['government','named'],
    title: 'Online Quiz on Safe & Responsible Use of AI',
    org: 'MeitY · ISEA · CDAC · Digital India · MyGov',
    date: 'Certificate of Participation',
    desc: 'Participated in the Online Quiz on Safe and Responsible Use of Artificial Intelligence organised by ISEA Project, Ministry of Electronics and Information Technology (MeitY), Government of India. Demonstrated knowledge of ethical and responsible AI usage.',
    tags: ['Government of India', 'Artificial Intelligence', 'MeitY', 'ISEA', 'MyGov', 'Digital India'],
    emoji: '🤖'
  }},
  {{
    type: 'named',
    category: ['internship','named'],
    title: 'Certificate of Completion — Web Dev Internship',
    org: 'Oasis Infobyte · AICTE OIB-SIP',
    date: '15 March 2026',
    desc: 'Completed a 1-month AICTE-recognised remote internship in Web Development and Designing at Oasis Infobyte (05 Feb – 15 Mar 2026). Built and deployed real-world web projects. Certified under ISO 9001:2015 standards. Certificate ID: OIB/F1/IP353.',
    tags: ['Internship', 'Web Development', 'AICTE', 'Oasis Infobyte', '2026', 'ISO 9001:2015'],
    emoji: '💼'
  }},
  {{
    type: 'named',
    category: ['internship','named'],
    title: 'Certificate of Appreciation — Star Performer',
    org: 'Oasis Infobyte · AICTE OIB-SIP',
    date: '15 March 2026',
    desc: 'Recognised as a ⭐ Star Performer of the AICTE Oasis Infobyte Internship for exceptional dedication and outstanding contributions — awarded a special Certificate of Appreciation, earning "Wonderful Remarks" from the program coordinator.',
    tags: ['Star Performer', 'Appreciation', 'AICTE', 'Oasis Infobyte', '2026'],
    emoji: '⭐'
  }},
  {{
    type: 'named',
    category: ['tech','named'],
    title: 'Python for Beginners',
    org: 'Verified Certificate',
    date: '25 March 2026',
    desc: 'Successfully completed the Python for Beginners course. Certificate Code: 10004012320260325_1. Demonstrated foundational Python programming skills including data types, control flow, functions, and basic problem solving.',
    tags: ['Python', 'Programming', 'Certificate', '2026', 'Beginner'],
    emoji: '🐍'
  }}
];

{drive_certs_js}

driveCerts = driveCerts.map(d => ({{
  type: 'drive',
  category: d.category || ['drive'],
  title: d.title,
  org: 'Verified Certificate · Google Drive',
  date: 'View Full Document',
  desc: 'Click "View Certificate" to preview this verified certificate directly from Google Drive.',
  tags: ['Verified Certificate', 'Google Drive'],
  driveId: d.driveId
}}));

let allCerts = [...namedCerts, ...driveCerts];

// Remove duplicates by title
allCerts = allCerts.filter((cert, index, self) =>
  index === self.findIndex(c => c.title.toLowerCase() === cert.title.toLowerCase())
);

document.addEventListener('DOMContentLoaded', () => {{
  const total = allCerts.length;
  const named = allCerts.filter(c => c.type === 'named').length;
  const drive = allCerts.filter(c => c.type === 'drive').length;
  document.getElementById('totalCount').textContent = total;
  document.getElementById('namedCount').textContent = named;
  document.getElementById('driveCount').textContent = drive;
  document.getElementById('totalCertCount').textContent = total;
  document.getElementById('subTotalText').textContent = total + " certifications and verified credentials";
}});

let currentFilter = 'all';
let currentSearch = '';

// ── RENDER CARDS ──
function renderCards() {{
  const grid = document.getElementById('certsGrid');
  const noRes = document.getElementById('noResults');
  const countEl = document.getElementById('visibleCount');

  let filtered = allCerts.filter(c => {{
    const matchFilter =
      currentFilter === 'all' ||
      c.category.includes(currentFilter);

    const q = currentSearch.toLowerCase();
    const matchSearch = !q ||
      c.title.toLowerCase().includes(q) ||
      c.org.toLowerCase().includes(q) ||
      (c.tags || []).some(t => t.toLowerCase().includes(q));

    return matchFilter && matchSearch;
  }});

  countEl.textContent = filtered.length;

  if (filtered.length === 0) {{
    grid.innerHTML = '';
    noRes.style.display = 'block';
    return;
  }}
  noRes.style.display = 'none';

  grid.innerHTML = filtered.map((c, i) => {{
    const idx = allCerts.indexOf(c);
    if (c.type === 'named') {{
      return `
      <div class="cert-card" onclick="openModal(${{idx}})">
        <div class="cert-thumb" style="background:linear-gradient(135deg,var(--surface),rgba(56,217,245,0.08));display:flex;align-items:center;justify-content:center;font-size:3.5rem;">
          ${{c.emoji}}
          <div class="cert-thumb-overlay"></div>
        </div>
        <span class="cert-type-badge badge-named" style="position:absolute;top:10px;right:10px;">Named Award</span>
        <div class="cert-body">
          <div class="cert-issuer">${{c.org}}</div>
          <div class="cert-name">${{c.title}}</div>
          <div class="cert-date">📅 ${{c.date}}</div>
          <div class="cert-desc">${{c.desc.slice(0, 110)}}${{c.desc.length > 110 ? '…' : ''}}</div>
          <div class="cert-tags">${{c.tags.map(t=>`<span class="cert-tag">${{t}}</span>`).join('')}}</div>
        </div>
        <div class="cert-footer">
          <button class="cert-view-btn" onclick="openModal(${{idx}});event.stopPropagation()">
            <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            View Details
          </button>
        </div>
      </div>`;
    }} else {{
      const thumb = `https://drive.google.com/thumbnail?id=${{c.driveId}}&sz=w400`;
      const link = `https://drive.google.com/file/d/${{c.driveId}}/view`;
      return `
      <div class="cert-card" onclick="openModal(${{idx}})">
        <div class="cert-thumb">
          <img src="${{thumb}}" alt="${{c.title}}" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
          <div class="cert-thumb-fallback" style="display:none;">📄</div>
          <div class="cert-thumb-overlay"></div>
          <span class="cert-type-badge badge-drive">Google Drive</span>
        </div>
        <div class="cert-body">
          <div class="cert-issuer">${{c.org}}</div>
          <div class="cert-name">${{c.title}}</div>
          <div class="cert-date">${{c.date}}</div>
          <div class="cert-tags">${{c.tags.map(t=>`<span class="cert-tag">${{t}}</span>`).join('')}}</div>
        </div>
        <div class="cert-footer">
          <button class="cert-view-btn" onclick="openModal(${{idx}});event.stopPropagation()">
            <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            View Certificate
          </button>
          <a href="${{link}}" target="_blank" rel="noopener noreferrer" class="cert-open-link" onclick="event.stopPropagation()">
            <svg width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
            Open
          </a>
        </div>
      </div>`;
    }}
  }}).join('');
}}

// ── MODAL ──
function openModal(idx) {{
  const c = allCerts[idx];
  let html = '';

  if (c.type === 'named') {{
    html = `
      <div style="background:linear-gradient(135deg,var(--surface2),rgba(56,217,245,0.06));padding:60px 32px 40px;text-align:center;font-size:4rem;border-radius:24px 24px 0 0;">${{c.emoji}}</div>
      <div class="modal-body">
        <span class="modal-badge badge-named">Named Award</span>
        <div class="modal-title">${{c.title}}</div>
        <div class="modal-org">${{c.org}}</div>
        <div class="modal-desc">${{c.desc}}</div>
        <div class="modal-meta">
          <span class="meta-chip">📅 ${{c.date}}</span>
          ${{c.tags.map(t=>`<span class="meta-chip">${{t}}</span>`).join('')}}
        </div>
        <div class="modal-actions">
          <a href="index.html#certificates" class="modal-btn-outline">← Back to Portfolio</a>
        </div>
      </div>`;
  }} else {{
    const preview = `https://drive.google.com/file/d/${{c.driveId}}/preview`;
    const open = `https://drive.google.com/file/d/${{c.driveId}}/view`;
    html = `
      <div class="modal-body" style="padding-top:32px;">
        <span class="modal-badge badge-drive">Verified Certificate</span>
        <div class="modal-title">${{c.title}}</div>
        <div class="modal-org">${{c.org}}</div>
        <div class="modal-drive-frame">
          <iframe src="${{preview}}" allowfullscreen></iframe>
          <div class="modal-drive-bar">
            <span class="modal-drive-label">${{c.title}} — Google Drive Preview</span>
            <a href="${{open}}" target="_blank" rel="noopener noreferrer" class="cert-view-btn" style="font-size:0.65rem;padding:6px 14px;">
              <svg width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
              Open Full
            </a>
          </div>
        </div>
        <div class="modal-meta">${{c.tags.map(t=>`<span class="meta-chip">${{t}}</span>`).join('')}}</div>
        <div class="modal-actions">
          <a href="${{open}}" target="_blank" rel="noopener noreferrer" class="modal-btn-primary">
            <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
            Open in Google Drive
          </a>
          <button class="modal-btn-outline" onclick="closeModal()">Close</button>
        </div>
      </div>`;
  }}

  document.getElementById('modalContent').innerHTML = html;
  document.getElementById('modalOverlay').classList.add('active');
  document.body.style.overflow = 'hidden';
}}

function closeModal(e) {{
  if (!e || e.target === document.getElementById('modalOverlay') || (e.target && e.target.classList.contains('modal-close'))) {{
    document.getElementById('modalOverlay').classList.remove('active');
    document.body.style.overflow = '';
  }}
}}

document.addEventListener('keydown', e => {{ if(e.key==='Escape') closeModal(); }});

// ── FILTERS ──
document.querySelectorAll('.filter-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentFilter = btn.getAttribute('data-filter');
    renderCards();
  }});
}});

// ── SEARCH ──
document.getElementById('searchInput').addEventListener('input', (e) => {{
  currentSearch = e.target.value;
  renderCards();
}});

// ── INITIALIZE ON PAGE LOAD ──
document.addEventListener('DOMContentLoaded', () => {{
  renderCards();
}});
</script>
</body>
</html>
"""

with open(r"c:\Users\Sanjay G L\Desktop\portfiler\certificates.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated new certificates.html with {len(drive_entries)+6} certificates!")
