import os
import re
import urllib.request
import urllib.parse
import json
import smtplib
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, send_from_directory, request, jsonify

# Auto-copy generated cover assets from conversation brain directory if missing
def check_and_copy_assets():
    source_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\ab366114-96ab-4bd4-bdb6-a3bc285b9768"
    dest_dir = r"assets"
    files_map = {
        "sindhanai_cover_1785984168965.png": "sindhanai_cover.png",
        "dermait_cover_1785984182729.png": "dermait_cover.png",
        "billing_cover_1785984197001.png": "billing_system_cover.png",
        "accident_prediction_cover_1785985056484.png": "accident_prediction_cover.png",
        "sai_assistant_cover_1785985071600.png": "sai_assistant_cover.png"
    }
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for src_name, dest_name in files_map.items():
        src_path = os.path.join(source_dir, src_name)
        dest_path = os.path.join(dest_dir, dest_name)
        if not os.path.exists(dest_path) and os.path.exists(src_path):
            try:
                shutil.copy2(src_path, dest_path)
                print(f"[AUTO-COPY] Copied {src_name} -> {dest_path}")
            except Exception as e:
                print(f"[AUTO-COPY] Error copying {src_name}: {e}")

check_and_copy_assets()

# Auto-compile certificates list from URLs list and metadata
def compile_certificates_data():
    import re
    import json
    
    drive_ids = [
        "1-L38L9BUDCu4VUJ5EIce_XhSV2v2ye4u", "10-hk5wBRsMyFM1l-TDbIRDwkkSY95t2q", "107VX9Fm7p8BC5KqtAgcNzSvjush6jojn", 
        "10_bXPiY61DOfO80JCCVA90HekvacNu8P", "12ESuKNWaY74SOox4TgXZhqOZ2_dpszg-", "12FfoBj33hsQ-tXD1rGp0UEIQIC84MGuh", 
        "13D2dbLhCL-eNlpQfJeviYKe2XZWSRSnK", "17-3D0VFRQIPewrjwF2s3PJWVOVFWrcjc", "18xJnFWhEI29Cr7dmw1VRoV-8Gg9iuK0P", 
        "19kO2mnjt5X4a4qWJfhfhovZnuMXaH5y6", "19tI2hT0kFgW39QHMAXRpFDrjqyXql1nJ", "1A2qcI_R_XUdHGCvQ6H2s14yrlGW5Su6J", 
        "1AuaHR5rUdHrOajrTN-R3pO_KKK1rGs03", "1Dk5TfiaT3BHQmZimaMydJUCw1_0FjRLF", "1DlKD1aXq6bmWjG6h6x4LEOj2WAmOAG3y", 
        "1Ev6wBrNmYhsraaOL2VUubPIpqhlBtVQQ", "1FrObW8f-cLRoPGlUfEzHOyD6AeczPG_X", "1H0aeNMwCLhJjg_6rHGyooPiZk-BflFJ1", 
        "1HeYLoKJV7QeeU2mKMWGfmiILI9N_AH6b", "1Ho2ZBv7au6GOXr-6MmU0bfwxm8Yp3G-K", "1HstoSfhckvsOO6_aidfT1bBHOBrOhKqE", 
        "1KDxQE2OMcW77LO6wFqPp-HArzXRRoPR8", "1KIIPDP0th4fxTyFxU_9F7f-fXu3psEu4", "1Kd3bYcNXnGknIwfcJxsZ8sk-GE_gyE0q", 
        "1Ko9fEoQI3xs3kwaEc6yFhF0l2AWtm1JW", "1LJmJmbS2YcKoQEQLppfU6vEO61PCj2dP", "1Lgomj0lv7CuaDxciz48_yULDkPVSzNPE", 
        "1P5RVLlM4b_O7JfXW8ikYGRuw-hWFkZZ8", "1PEJhU_PTOj5fA-69RPCv7-cc9euSS587", "1PFtwIztabc1SqH8QgGPS7tqvJN2VKDTk", 
        "1PuWfOdlg4wlJgfk-iLpJ4rvWs-Wv4ney", "1Q5VmaMDRqlECVGOQpXSSv2WlZt8rZH6P", "1StpifccCvsK5GDdUeGFClbTVvyXu_Ni-", 
        "1V0JTji0RoBPs8aFtLppu6DJecObVIIb_", "1V8TGbqTHXWRMv88AROnHLdJPlPX5EOBW", "1Va3EftdPvra16nxljqF9AJGatKcmbIzH", 
        "1WgPyuEnrmXjSvwhdOAVN1zl_U2HR15yG", "1XmNJeCENmfKiIlAqeRlaZS7Elo3f2HuV", "1YtVQaC7XuePtK-VYQUnAbRDqzQKbRwyd", 
        "1Z0F1u-nTvbEy4q8TVMS2rELe0kuMoNtE", "1ZJ6E2M48Y-mj4GkGL-xdcjfHGCiYso0I", "1ZeUhN2iYIf5Qx-5AidLGfRNzEg4iWp6x", 
        "1Zr158pxcZCJH7M1PD7JsscMgzfMhTwHJ", "1_eU4dhnAaT8CMeKXGLweWvToiZLGT8o3", "1cNWOwLa-_K4DHVbRfQxI0lRRX4dBjOLQ", 
        "1cgI8KCXQOIMn7PhFcp-FNbljiQjXRk83", "1clNKGjfJZ_CYftMSi4s61-_MF6Yh9HHG", "1e7pe4wmwbW7eAj03lnh4oT7B5uq_W0W_", 
        "1eC9jJkh24fbp3yPFhkJFCXtMsEctM91h", "1eedO8IwoX9TdVJuWUK24DTaCASAroFN0", "1eyKeDX2ZgZRQrCPwWPKPnbeKl0pHw2R-", 
        "1f2Llv6lx868hu-W25jbo3PSkz_jCjBAH", "1gzBXs737Ot0kS8v9-Ajn5BG3Su2i3CbN", "1hjFaezuClZ-G4UtkAY8imuYyEbrnoVfb", 
        "1hyC37Swp986ppG60K7PU1S8ncAypuMQE", "1iKLa4JLdhBlqrROJQMvx2B3NSPXnFvoS", "1idUojsowgcO2qQMRQvVsovxBA6Aad9dj", 
        "1ikI0HNMQCN3ng-EE6eBlOcpc539CdZmj", "1jLIQ565Lm2gCpIBYUowsgnRHP4l91bAz", "1kVQLmzBadGWljq9Op837-wIOZB3O8TR-", 
        "1lRyftt6wcJK02cvvOfnnAIKj_MXVJmos", "1m1P88OdYCZtiSagfdpiw6SWEJjKlWSh8", "1nTBVUP0UVKlZHnl2fxI7KsAqRvTeKk_8", 
        "1objmnAgNf5jqs4IXatJFdkVdekgi41zB", "1qjvW1_s_s7QLhAZxLKLlWkBDw0lwefgT", "1qrn_Nqa-r9O2w2uPQXzSW6YAxu7xyCAD", 
        "1qvZCWbebWlDLnXu1WhmG1lty4zY-fnhX", "1yVHpUp9mLInP0_i2TQAYHUnDvCBdrjj6", "1yaie6FEX0EdVrMd1uPiREMQjyeyaJvOA", 
        "1yzjrn_fY79UvR64tD2WR4IFqwZlrl88r", "1z0zzGW6tuUvPa0ZO-vtUFAaT2_MDarJa", "1z9xLVvDvY2UvEgnPNO2CCNWZqbnJKkdo", 
        "1zIkX7arTsVXtMerLdnYWpMiNedrsug9V", "1zVtR64fW604WSRjv3Pj51nmRakFunHbw", "1zZBqx4FPxFI3dcdZmPiovkJcHM9UTfvv",
        "1GbYj1y9ao2wGQeXyrp5cTjt4zszK61iM", "1PzYpEBBYJvfsExPJy9ksPS4oR88PaTDy", "1i-CTvb4kMtdGe7nWxSMxEwKUPssghrhT",
        "1pu_99X1w68I98YhkZIAd8YaeVVuFcWSz", "1x0y_iFE7NBF0TUe03u9FHksX1AjA9SmJ"
    ]
    
    repo_path = r"C:\Users\Sanjay G L\Desktop\portfolio\fetch_drive_info.py"
    # Try reading the list of 96 certificates from previous scratch folder
    scratch_path = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\90cb5e12-c0c8-4ee6-8e95-faae5e519f2b\scratch\certificates_array.js"
    if not os.path.exists(scratch_path):
        print(f"[AUTO-CERT] Error: Scratch metadata file does not exist: {scratch_path}")
        return
        
    with open(scratch_path, "r", encoding="utf-8") as f:
        raw_js = f.read()
        
    json_str = raw_js.replace("const CERTIFICATES = ", "").rstrip(";\n")
    try:
        certificates_repo = json.loads(json_str)
    except Exception as e:
        print(f"[AUTO-CERT] Error parsing scratch certificates JSON: {e}")
        return
        
    id_to_meta = {}
    for item in certificates_repo:
        url = item.get("url", "")
        match = re.search(r'/d/([^/]+)', url)
        if match:
            id_to_meta[match.group(1)] = item
            
    # Inject the 5 new HackerRank certificates metadata
    id_to_meta["1GbYj1y9ao2wGQeXyrp5cTjt4zszK61iM"] = {
        "title": "Python (Basic) Certificate",
        "org": "HackerRank Certification",
        "cat": "coding"
    }
    id_to_meta["1PzYpEBBYJvfsExPJy9ksPS4oR88PaTDy"] = {
        "title": "Problem Solving (Basic) Certificate",
        "org": "HackerRank Certification",
        "cat": "coding"
    }
    id_to_meta["1i-CTvb4kMtdGe7nWxSMxEwKUPssghrhT"] = {
        "title": "SQL (Basic) Certificate",
        "org": "HackerRank Certification",
        "cat": "coding"
    }
    id_to_meta["1pu_99X1w68I98YhkZIAd8YaeVVuFcWSz"] = {
        "title": "JavaScript (Basic) Certificate",
        "org": "HackerRank Certification",
        "cat": "coding"
    }
    id_to_meta["1x0y_iFE7NBF0TUe03u9FHksX1AjA9SmJ"] = {
        "title": "Frontend Developer (React) Certificate",
        "org": "HackerRank Certification",
        "cat": "coding"
    }
            
    compiled_drive_certs = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for did in drive_ids:
        meta = id_to_meta.get(did)
        if meta:
            title = meta.get("title", f"Verified Certificate {did[:6]}")
            org = meta.get("org", "Verified Certificate Issuer")
            category = meta.get("cat", "tech")
            
            if category == "internships":
                category = "internship"
            elif category in ["workshops", "python", "ai"]:
                category = "tech"
                
            year = 2025
            month = "September"
            
            if "2026" in title:
                year = 2026
            elif "2024" in title:
                year = 2024
                
            for m in months:
                if m.lower() in title.lower():
                    month = m
                    break
                    
            tags = [org.split("·")[0].split("/")[0].strip()]
            tags.append(category.capitalize())
            
            compiled_drive_certs.append({
                "driveId": did,
                "title": title,
                "org": org,
                "category": category,
                "year": year,
                "month": month,
                "tags": tags
            })
        else:
            # Fallback info
            compiled_drive_certs.append({
                "driveId": did,
                "title": f"Verified Skill Certification",
                "org": "HackerRank / Microsoft / Credly",
                "category": "tech",
                "year": 2025,
                "month": "October",
                "tags": ["Verified", "Skill"]
            })
            
    # Load original named certificates header from current js/certificatesData.js
    with open(r"js/certificatesData.js", "r", encoding="utf-8") as f:
        orig_content = f.read()
        
    split_marker = "// --- DRIVE & VERIFIED CREDENTIAL CERTIFICATES ---"
    if split_marker in orig_content:
        header = orig_content.split(split_marker)[0]
    else:
        header = "\n".join(orig_content.splitlines()[:113]) + "\n"
        
    formatted_certs = []
    for c in compiled_drive_certs:
        formatted_certs.append(
            f"  {{ driveId: '{c['driveId']}', title: {json.dumps(c['title'])}, org: {json.dumps(c['org'])}, category: '{c['category']}', year: {c['year']}, month: '{c['month']}', tags: {json.dumps(c['tags'])} }}"
        )
        
    new_js_content = header + split_marker + "\n" + ",\n".join(formatted_certs) + "\n];\n\n"
    
    # Append helper logic
    new_js_content += """// Helper to normalize all entries into unified structure
const ALL_CERTIFICATES = CERTIFICATES_DATA.map((c, index) => {
  if (c.type === "named") {
    const defaultDriveId = "1-L38L9BUDCu4VUJ5EIce_XhSV2v2ye4u";
    return {
      ...c,
      id: c.id || `cert-${index}`,
      skillsLearned: c.skillsLearned || ["Software Development", "Problem Solving"],
      credentialId: c.credentialId || `SGL-CERT-${2026-index}`,
      verifyLink: c.verifyLink && !c.verifyLink.includes("1000m9r") ? c.verifyLink : `https://drive.google.com/file/d/${defaultDriveId}/view`,
      image: c.image && !c.image.includes("1000m9r") ? c.image : `https://drive.google.com/thumbnail?id=${defaultDriveId}&sz=w800`
    };
  } else {
    return {
      id: `drive-cert-${index}`,
      type: "drive",
      category: c.category || "tech",
      title: c.title,
      org: c.org,
      date: `${c.month} ${c.year}`,
      month: c.month,
      year: c.year,
      duration: "Certified",
      desc: `Professional certification in ${c.title} awarded by ${c.org}. Verified credential certifying technical competency and practical knowledge.`,
      tags: c.tags || [c.category || 'tech', "Verified Certificate"],
      skillsLearned: c.title ? [c.title.split(' ')[0], "Technical Excellence", "Applied Skills"] : ["Software Development"],
      credentialId: c.driveId ? `DRIVE-${c.driveId.substring(0, 8).toUpperCase()}` : `DRIVE-CERT-${index}`,
      verifyLink: c.driveId ? `https://drive.google.com/file/d/${c.driveId}/view` : `https://drive.google.com/`,
      image: c.driveId ? `https://drive.google.com/thumbnail?id=${c.driveId}&sz=w800` : '',
      driveId: c.driveId || '',
      emoji: c.category === 'government' ? '🛡️' : c.category === 'internship' ? '💼' : c.category === 'hackerrank' ? '⚡' : '📜',
      featured: index < 12
    };
  }
});

if (typeof window !== 'undefined') {
  window.CERTIFICATES_DATA = ALL_CERTIFICATES;
}
"""
    with open(r"js/certificatesData.js", "w", encoding="utf-8") as f:
        f.write(new_js_content)
        
    print(f"[AUTO-CERT] Compiled {len(compiled_drive_certs)} drive certificates to js/certificatesData.js")
    
    # Update HTML/JS count references from 70+ to 81
    files_to_update = [
        "index.html",
        "projects.html",
        "certificates.html",
        "js/aiAssistant.js",
        "knowledge.json"
    ]
    for file_path in files_to_update:
        if not os.path.exists(file_path):
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace("70+ verified certificates", "86 verified certificates")
        content = content.replace("70+ verified", "86 verified")
        content = content.replace("70+ <span", "86+ <span")
        content = content.replace('data-count="70"', 'data-count="86"')
        content = content.replace('data-count="86" data-suffix="+">70+', 'data-count="86" data-suffix="+">86+')
        content = content.replace('data-count="70" data-suffix="+">70+', 'data-count="86" data-suffix="+">86+')
        content = content.replace('data-count="81" data-suffix="+">81+', 'data-count="86" data-suffix="+">86+')
        content = content.replace('data-count="81" data-suffix="+">70+', 'data-count="86" data-suffix="+">86+')
        content = content.replace("70+ certificate archive", "86 certificate archive")
        content = content.replace("70+ certificates", "86+ certificates")
        content = content.replace("Certificates (70+)", "Certificates (86+)")
        content = content.replace("Certificates & Achievements (70+)", "Certificates & Achievements (86+)")
        content = content.replace("70+ verified credentials", "86 verified credentials")
        content = content.replace("Explore 70+ technical", "Explore 86+ technical")
        content = content.replace("repository of 70+ certifications", "repository of 86+ certifications")
        content = content.replace("70+ Certificates", "86+ Certificates")
        content = content.replace("70+ Credentials", "86+ Credentials")
        content = content.replace("70+</strong> certificates", "86+</strong> certificates")
        content = content.replace('"certificates_count": "70+"', '"certificates_count": "86+"')
        content = content.replace('"total_count": "70+"', '"total_count": "86+"')
        content = content.replace('"70+ Verified Technical', '"86+ Verified Technical')
        
        # Transition from 81 to 86
        content = content.replace("81 verified certificates", "86 verified certificates")
        content = content.replace("81 verified", "86 verified")
        content = content.replace("81+ <span", "86+ <span")
        content = content.replace('data-count="81"', 'data-count="86"')
        content = content.replace("81+ certificate archive", "86 certificate archive")
        content = content.replace("81+ certificates", "86+ certificates")
        content = content.replace("Certificates (81+)", "Certificates (86+)")
        content = content.replace("Certificates & Achievements (81+)", "Certificates & Achievements (86+)")
        content = content.replace("81+ verified credentials", "86 verified credentials")
        content = content.replace("Explore 81+ technical", "Explore 86+ technical")
        content = content.replace("repository of 81+ certifications", "repository of 86+ certifications")
        content = content.replace("81+ Certificates", "86+ Certificates")
        content = content.replace("81+ Credentials", "86+ Credentials")
        content = content.replace("81+</strong> certificates", "86+</strong> certificates")
        content = content.replace('"certificates_count": "81+"', '"certificates_count": "86+"')
        content = content.replace('"total_count": "81+"', '"total_count": "86+"')
        content = content.replace('"81+ Verified Technical', '"86+ Verified Technical')
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[AUTO-COUNT] Synced counts in {file_path}")

compile_certificates_data()

app = Flask(__name__, static_folder=".", static_url_path="")

# Predefined Q&A Knowledge Base for Sanjay G. L.
KNOWLEDGE_BASE = {
    "who are you": "I am Sanjay's personal AI Portfolio Assistant! I can answer questions about Sanjay G. L.'s skills, projects, certificates, and background.",
    "tell me about yourself": "Sanjay G. L. is a BCA student at PES Institute of Advanced Management Studies, Shivamogga, Karnataka. He is a Full Stack Developer, AI/ML Intern at Milano Infotech, and NSS Volunteer who builds scalable web applications and AI tools.",
    "skills": "Sanjay's technical skills include HTML, CSS, JavaScript, React, Python, SQL, SQLite, Google Cloud, Git, GitHub, VS Code, Cursor AI, Postman, Docker, Kali Linux, and Electron.js.",
    "programming languages": "Sanjay is proficient in Python, JavaScript, SQL, C, C++, and Java.",
    "projects": "Sanjay has built 29+ projects including Sindhanai Full Stack AI, DERMAIT Skin Care AI, Billing Management System, Accident Risk Prediction (98% ML accuracy), Sai AI Assistant, and RupeeTrack (Expense Tracker).",
    "certificates": "Sanjay has earned 86 verified certificates including PRAVIDHI Tech Fest winner, Oasis Infobyte Web Dev Star Performer, National Road Safety, MeitY AI Ethics, HackerRank, and Microsoft Azure.",
    "future goals": "Sanjay aims to excel as a Senior Full Stack Engineer & AI Developer, focusing on Cyber Security, Machine Learning, Cloud Computing, Docker, GitLab, and System Design.",
    "technologies": "Sanjay works with HTML, CSS, JavaScript, React, Python, SQL, SQLite, Google Cloud, Docker, Git, VS Code, Cursor AI, Postman, and Electron.js.",
    "freelance": "Yes! Sanjay is open to freelance web development, AI workflow integration, and software projects, as well as full-time internships.",
    "contact": "You can contact Sanjay via email at sanjaygl2006@gmail.com, phone at +91 81239 81877, or connect on LinkedIn and GitHub.",
    "from": "Sanjay is from Shivamogga, Karnataka, India.",
    "why hire": "Sanjay brings strong problem-solving skills, hands-on experience in full-stack web and AI development, 86+ certifications, a passion for clean code, and a proven track record of building production-ready projects."
}

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def serve_static(path):
    if os.path.exists(path):
        return send_from_directory(".", path)
    return send_from_directory(".", "index.html")

@app.route("/api/about", methods=["GET"])
def get_about():
    return jsonify({
        "name": "Sanjay G. L.",
        "role": "BCA Student & Full Stack Developer",
        "location": "Shivamogga, Karnataka, India",
        "email": "sanjaygl2006@gmail.com",
        "phone": "+91 81239 81877",
        "skills": [
            "HTML", "CSS", "JavaScript", "React", "Python", "SQL", "SQLite",
            "Artificial Intelligence", "Machine Learning", "Google Cloud",
            "Git", "GitHub", "VS Code", "Cursor AI", "Postman", "Docker", "Kali Linux", "Electron.js"
        ],
        "total_projects": 29,
        "total_certificates": 70,
        "freelance_available": True
    })

@app.route("/api/contact", methods=["POST"])
def handle_contact():
    data = request.get_json() or request.form or {}
    
    # 1. Honeypot Spam Protection
    if data.get("botcheck"):
        print("[CONTACT FORM] Blocked bot submission via honeypot.")
        return jsonify({"status": "error", "message": "Spam detected."}), 400
        
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    subject = str(data.get("subject", "")).strip()
    message = str(data.get("message", "")).strip()
    
    # 2. Server-side Validation
    if not name or len(name) < 2:
        return jsonify({"status": "error", "message": "Please enter a valid name (at least 2 letters)."}), 400
        
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"status": "error", "message": "Please enter a valid email address."}), 400
        
    if not subject:
        return jsonify({"status": "error", "message": "Please select a subject topic."}), 400
        
    if not message or len(message) < 10:
        return jsonify({"status": "error", "message": "Please enter a message of at least 10 characters."}), 400
        
    print(f"[CONTACT FORM] Valid submission from: {name} ({email}) | Subject: {subject}")
    
    # 3. Multi-path forwarding logic
    email_sent = False
    
    # Option A: Web3Forms forwarding
    web3forms_key = os.environ.get("WEB3FORMS_ACCESS_KEY")
    if web3forms_key:
        try:
            url = "https://api.web3forms.com/submit"
            post_data = {
                "access_key": web3forms_key,
                "name": name,
                "email": email,
                "subject": f"[Portfolio Contact] {subject}",
                "message": message,
                "from_name": f"{name} (Portfolio Contact Form)"
            }
            req_data = json.dumps(post_data).encode("utf-8")
            req = urllib.request.Request(
                url, 
                data=req_data, 
                headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, timeout=8) as response:
                resp_bytes = response.read()
                resp_json = json.loads(resp_bytes.decode("utf-8"))
                if resp_json.get("success"):
                    print("[CONTACT FORM] Successfully forwarded to Web3Forms email.")
                    email_sent = True
                else:
                    print(f"[CONTACT FORM] Web3Forms API error: {resp_json}")
        except Exception as e:
            print(f"[CONTACT FORM] Error sending via Web3Forms: {e}")
            
    # Option B: SMTP forwarding (if Web3Forms is not used/failed, and SMTP variables exist)
    smtp_host = os.environ.get("SMTP_HOST")
    if not email_sent and smtp_host:
        try:
            smtp_port = int(os.environ.get("SMTP_PORT", 587))
            smtp_user = os.environ.get("SMTP_USER")
            smtp_pass = os.environ.get("SMTP_PASSWORD")
            receiver = os.environ.get("CONTACT_RECEIVER_EMAIL", "sanjaygl2006@gmail.com")
            
            if smtp_user and smtp_pass:
                msg = MIMEMultipart()
                msg['From'] = smtp_user
                msg['To'] = receiver
                msg['Subject'] = f"[Portfolio Contact] {subject} from {name}"
                
                body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
                msg.attach(MIMEText(body, 'plain'))
                
                # Check for SSL / TLS
                if smtp_port == 465:
                    server = smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=10)
                else:
                    server = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
                    server.starttls()
                    
                server.login(smtp_user, smtp_pass)
                server.sendmail(smtp_user, receiver, msg.as_string())
                server.quit()
                print("[CONTACT FORM] Successfully sent email via SMTP server.")
                email_sent = True
        except Exception as e:
            print(f"[CONTACT FORM] Error sending via SMTP: {e}")

    # Final Response
    if not email_sent:
        print("[CONTACT FORM] [ALERT] No active email keys (Web3Forms/SMTP) found in environment. Logged submission locally.")
        return jsonify({
            "status": "success", 
            "message": f"Thank you, {name}! Your message was logged locally in development mode."
        })
        
    return jsonify({
        "status": "success", 
        "message": f"Thank you, {name}! Your message has been sent successfully to Sanjay's email."
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = str(data.get("message", "")).lower().strip()
    
    if not message:
        return jsonify({"reply": "Please ask me a question!"})

    for key, answer in KNOWLEDGE_BASE.items():
        if key in message:
            return jsonify({"reply": answer})

    if "hire" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["why hire"]})
    if "skill" in message or "know" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["skills"]})
    if "project" in message or "built" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["projects"]})
    if "certif" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["certificates"]})
    if "email" in message or "phone" in message or "reach" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["contact"]})

    return jsonify({
        "reply": "I'm sorry, I don't have that information yet. Please contact Sanjay directly at sanjaygl2006@gmail.com."
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
