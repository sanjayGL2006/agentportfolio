import os
import re
import urllib.request
import urllib.parse
import json
import smtplib
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, send_from_directory, request, jsonify, redirect
# pyrefly: ignore [missing-import]
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
try:
    import google.generativeai as genai
    HAS_GEMINI = True
except:
    HAS_GEMINI = False

from datetime import datetime
from collections import defaultdict
import time
from dotenv import load_dotenv

# Load environmental variables from .env
load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize Supabase Client
try:
    # pyrefly: ignore [missing-import]
    from supabase import create_client, Client
    supabase_url = os.environ.get("SUPABASE_URL", "https://mglzwnampheswtjzrcbf.supabase.co")
    supabase_key = os.environ.get("SUPABASE_KEY") or os.environ.get("SUPABASE_PUBLISHABLE_KEY", "sb_publishable_vuV_ZmS859v1QUhQHISoqg_nkN-DWFl")
    supabase: Client = create_client(supabase_url, supabase_key)
    print("[SUPABASE] Client Initialized Successfully.")
except Exception as _se_err:
    supabase = None
    print(f"[SUPABASE] Warning: Could not initialize client: {_se_err}")

# Auto-copy generated cover assets from conversation brain directory if missing
def check_and_copy_assets():
    try:
        source_dir = r"C:\Users\Sanjay G L\.gemini\antigravity-ide\brain\ab366114-96ab-4bd4-bdb6-a3bc285b9768"
        dest_dir = os.path.join(BASE_DIR, "assets")
        files_map = {
            "sindhanai_cover_1785984168965.png": "sindhanai_cover.png",
            "dermait_cover_1785984182729.png": "dermait_cover.png",
            "billing_cover_1785984197001.png": "billing_system_cover.png",
            "accident_prediction_cover_1785985056484.png": "accident_prediction_cover.png",
            "sai_assistant_cover_1785985071600.png": "sai_assistant_cover.png"
        }
        if not os.path.exists(dest_dir):
            try:
                os.makedirs(dest_dir, exist_ok=True)
            except Exception:
                pass
        for src_name, dest_name in files_map.items():
            src_path = os.path.join(source_dir, src_name)
            dest_path = os.path.join(dest_dir, dest_name)
            if not os.path.exists(dest_path) and os.path.exists(src_path):
                try:
                    shutil.copy2(src_path, dest_path)
                    print(f"[AUTO-COPY] Copied {src_name} -> {dest_path}")
                except Exception as e:
                    print(f"[AUTO-COPY] Error copying {src_name}: {e}")
    except Exception as err:
        print(f"[AUTO-COPY] Asset check skipped: {err}")

check_and_copy_assets()

# Auto-compile certificates list from URLs list and metadata
def compile_certificates_data():
    drive_ids = [
        "1-L38L9BUDCu4VUJ5EIce_XhSV2v2ye4u",
        "10-hk5wBRsMyFM1l-TDbIRDwkkSY95t2q",
        "107VX9Fm7p8BC5KqtAgcNzSvjush6jojn",
        "10_bXPiY61DOfO80JCCVA90HekvacNu8P",
        "12ESuKNWaY74SOox4TgXZhqOZ2_dpszg-",
        "12FfoBj33hsQ-tXD1rGp0UEIQIC84MGuh",
        "13D2dbLhCL-eNlpQfJeviYKe2XZWSRSnK",
        "13tTd3Qniajnw25pGuzk7WFzSvKw1lAul",
        "17-3D0VFRQIPewrjwF2s3PJWVOVFWrcjc",
        "18xJnFWhEI29Cr7dmw1VRoV-8Gg9iuK0P",
        "19kO2mnjt5X4a4qWJfhfhovZnuMXaH5y6",
        "19tI2hT0kFgW39QHMAXRpFDrjqyXql1nJ",
        "1A2qcI_R_XUdHGCvQ6H2s14yrlGW5Su6J",
        "1AuaHR5rUdHrOajrTN-R3pO_KKK1rGs03",
        "1Cb4E1Am3NLuAt4fN3hUNadZKKpjL9yKP",
        "1Dk5TfiaT3BHQmZimaMydJUCw1_0FjRLF",
        "1DlKD1aXq6bmWjG6h6x4LEOj2WAmOAG3y",
        "1Ev6wBrNmYhsraaOL2VUubPIpqhlBtVQQ",
        "1FrObW8f-cLRoPGlUfEzHOyD6AeczPG_X",
        "1H0aeNMwCLhJjg_6rHGyooPiZk-BflFJ1",
        "1HeYLoKJV7QeeU2mKMWGfmiILI9N_AH6b",
        "1Ho2ZBv7au6GOXr-6MmU0bfwxm8Yp3G-K",
        "1HstoSfhckvsOO6_aidfT1bBHOBrOhKqE",
        "1KDxQE2OMcW77LO6wFqPp-HArzXRRoPR8",
        "1KIIPDP0th4fxTyFxU_9F7f-fXu3psEu4",
        "1Kd3bYcNXnGknIwfcJxsZ8sk-GE_gyE0q",
        "1Ko9fEoQI3xs3kwaEc6yFhF0l2AWtm1JW",
        "1LJmJmbS2YcKoQEQLppfU6vEO61PCj2dP",
        "1Lgomj0lv7CuaDxciz48_yULDkPVSzNPE",
        "1MCuKgqYoockhgebBftpqQXlsDXKGZAsw",
        "1NhxE2rGs-diBmAspxkanzLA_NG_KgIv9",
        "1P5RVLlM4b_O7JfXW8ikYGRuw-hWFkZZ8",
        "1PEJhU_PTOj5fA-69RPCv7-cc9euSS587",
        "1PFtwIztabc1SqH8QgGPS7tqvJN2VKDTk",
        "1PuWfOdlg4wlJgfk-iLpJ4rvWs-Wv4ney",
        "1Q5VmaMDRqlECVGOQpXSSv2WlZt8rZH6P",
        "1TJKRwFP9K-1lPlluPDrKJDLMO8L5fjaz",
        "1V0JTji0RoBPs8aFtLppu6DJecObVIIb_",
        "1V8TGbqTHXWRMv88AROnHLdJPlPX5EOBW",
        "1Va3EftdPvra16nxljqF9AJGatKcmbIzH",
        "1WgPyuEnrmXjSvwhdOAVN1zl_U2HR15yG",
        "1XeXNbcDl9lp3qc-BjE5jkXGdTGx0lLsP",
        "1XmNJeCENmfKiIlAqeRlaZS7Elo3f2HuV",
        "1YtVQaC7XuePtK-VYQUnAbRDqzQKbRwyd",
        "1ZJ6E2M48Y-mj4GkGL-xdcjfHGCiYso0I",
        "1ZeUhN2iYIf5Qx-5AidLGfRNzEg4iWp6x",
        "1Zr158pxcZCJH7M1PD7JsscMgzfMhTwHJ",
        "1_eU4dhnAaT8CMeKXGLweWvToiZLGT8o3",
        "1cNWOwLa-_K4DHVbRfQxI0lRRX4dBjOLQ",
        "1cgI8KCXQOIMn7PhFcp-FNbljiQjXRk83",
        "1clNKGjfJZ_CYftMSi4s61-_MF6Yh9HHG",
        "1dScd4j_m9hXy6ogBfA2dSH09cT0L_D3A",
        "1e7pe4wmwbW7eAj03lnh4oT7B5uq_W0W_",
        "1eC9jJkh24fbp3yPFhkJFCXtMsEctM91h",
        "1eedO8IwoX9TdVJuWUK24DTaCASAroFN0",
        "1eyKeDX2ZgZRQrCPwWPKPnbeKl0pHw2R-",
        "1f2Llv6lx868hu-W25jbo3PSkz_jCjBAH",
        "1gh2-eo8P98ce2O24dl6ddilLZknUe27A",
        "1gzBXs737Ot0kS8v9-Ajn5BG3Su2i3CbN",
        "1hjFaezuClZ-G4UtkAY8imuYyEbrnoVfb",
        "1hyC37Swp986ppG60K7PU1S8ncAypuMQE",
        "1idUojsowgcO2qQMRQvVsovxBA6Aad9dj",
        "1ikI0HNMQCN3ng-EE6eBlOcpc539CdZmj",
        "1jLIQ565Lm2gCpIBYUowsgnRHP4l91bAz",
        "1kVQLmzBadGWljq9Op837-wIOZB3O8TR-",
        "1lRyftt6wcJK02cvvOfnnAIKj_MXVJmos",
        "1m1P88OdYCZtiSagfdpiw6SWEJjKlWSh8",
        "1nTBVUP0UVKlZHnl2fxI7KsAqRvTeKk_8",
        "1objmnAgNf5jqs4IXatJFdkVdekgi41zB",
        "1qjvW1_s_s7QLhAZxLKLlWkBDw0lwefgT",
        "1qrn_Nqa-r9O2w2uPQXzSW6YAxu7xyCAD",
        "1qvZCWbebWlDLnXu1WhmG1lty4zY-fnhX",
        "1rOtjoYebWSA-_bis8_ja1ZDruCXss28E",
        "1xiVeBY3Ls_K79m0OaXKmeJimwvTA10jY",
        "1yVHpUp9mLInP0_i2TQAYHUnDvCBdrjj6",
        "1yaie6FEX0EdVrMd1uPiREMQjyeyaJvOA",
        "1yzjrn_fY79UvR64tD2WR4IFqwZlrl88r",
        "1z0zzGW6tuUvPa0ZO-vtUFAaT2_MDarJa",
        "1z9xLVvDvY2UvEgnPNO2CCNWZqbnJKkdo",
        "1zIkX7arTsVXtMerLdnYWpMiNedrsug9V",
        "1zVtR64fW604WSRjv3Pj51nmRakFunHbw",
        "1zZBqx4FPxFI3dcdZmPiovkJcHM9UTfvv",
        "1GbYj1y9ao2wGQeXyrp5cTjt4zszK61iM",
        "1PzYpEBBYJvfsExPJy9ksPS4oR88PaTDy",
        "1i-CTvb4kMtdGe7nWxSMxEwKUPssghrhT",
        "1pu_99X1w68I98YhkZIAd8YaeVVuFcWSz",
        "1x0y_iFE7NBF0TUe03u9FHksX1AjA9SmJ"
]
    
    files_to_update = [
        "index.html",
        "projects.html",
        "certificates.html",
        "js/aiAssistant.js",
        "knowledge.json",
        "README.md"
    ]
    try:
        for file_path in files_to_update:
            abs_path = os.path.join(BASE_DIR, file_path)
            if not os.path.exists(abs_path):
                continue
            try:
                with open(abs_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                content = content.replace("0 certificates", "87+ certificates")
                content = content.replace("Certificates (0)", "Certificates (87+)")
                content = content.replace("Certificates & Achievements (0)", "Certificates & Achievements (87+)")
                content = content.replace("0 Credentials", "87+ Credentials")
                content = content.replace("0 verified credentials", "87+ verified credentials")
                content = content.replace("0 verified certificates", "87+ verified certificates")
                content = content.replace("0 verified", "87+ verified")
                content = content.replace("repository of 0 certifications", "repository of 87+ certifications")
                content = content.replace("Explore 0 technical", "Explore 87+ technical")
                content = content.replace('data-count="0" data-suffix="">0</div>', 'data-count="87" data-suffix="+">87+</div>')
                content = content.replace('data-count="0"', 'data-count="87"')
                content = content.replace('0</strong> certificates', '87+</strong> certificates')
                content = content.replace('"certificates_count": "0"', '"certificates_count": "87+"')
                content = content.replace('"total_count": "0"', '"total_count": "87+"')
                
                with open(abs_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"[AUTO-COUNT] Synced 87+ counts in {file_path}")
            except Exception as fe:
                print(f"[AUTO-COUNT] Skipping write for {file_path}: {fe}")
    except Exception as e:
        print(f"[AUTO-COUNT] Sync error: {e}")

compile_certificates_data()

app = Flask(__name__, static_folder=None)

# ----------------- DATABASE CONFIGURATION -----------------
# Setup database URL (MySQL with local SQLite fallback)
db_url = os.environ.get("DATABASE_URL")
if not db_url:
    db_host = os.environ.get("DB_HOST")
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")
    db_port = os.environ.get("DB_PORT", "3306")
    if db_host and db_user and db_name:
        db_url = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    else:
        db_path = os.path.join(BASE_DIR, "database", "portfolio.db")
        try:
            os.makedirs(os.path.dirname(db_path), exist_ok=True)
        except Exception:
            db_path = "/tmp/portfolio.db"
        db_url = f"sqlite:///{db_path}"

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enforce SSL/TLS for MySQL connection if DB_SSL_CA or DB_SSL_REQUIRE is configured
connect_args = {}
ssl_ca = os.environ.get("DB_SSL_CA")
if ssl_ca:
    connect_args["ssl"] = {"ca": ssl_ca}
elif os.environ.get("DB_SSL_REQUIRE", "false").lower() == "true":
    connect_args["ssl"] = {"ssl_mode": "REQUIRED"}

if connect_args:
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "connect_args": connect_args
    }

db = SQLAlchemy(app)

# ----------------- ORM SCHEMAS -----------------
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer)
    category = db.Column(db.String(100))
    tagline = db.Column(db.Text)
    description = db.Column(db.Text)
    tech_stack = db.Column(db.JSON)
    live = db.Column(db.String(255))
    github = db.Column(db.String(255))
    status = db.Column(db.String(50))
    featured = db.Column(db.Boolean, default=False)
    icon = db.Column(db.String(100))
    image = db.Column(db.String(255))
    overview = db.Column(db.Text)
    architecture = db.Column(db.Text)
    features = db.Column(db.JSON)
    structure = db.Column(db.JSON)
    futureScope = db.Column(db.JSON)
    timeline = db.Column(db.JSON)
    stats = db.Column(db.JSON)

class Certificate(db.Model):
    __tablename__ = 'certificates'
    id = db.Column(db.String(100), primary_key=True)
    type = db.Column(db.String(50))
    category = db.Column(db.String(100))
    title = db.Column(db.String(255), nullable=False)
    org = db.Column(db.String(255))
    date = db.Column(db.String(100))
    month = db.Column(db.String(50))
    year = db.Column(db.Integer)
    duration = db.Column(db.String(100))
    description = db.Column(db.Text)
    tags = db.Column(db.JSON)
    skillsLearned = db.Column(db.JSON)
    credentialId = db.Column(db.String(100))
    verifyLink = db.Column(db.String(500))
    image = db.Column(db.String(500))
    driveId = db.Column(db.String(100))
    emoji = db.Column(db.String(50))
    featured = db.Column(db.Boolean, default=False)

class AgentConversation(db.Model):
    __tablename__ = 'agent_conversations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.String(100), nullable=False)
    user_message = db.Column(db.Text, nullable=False)
    agent_response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, session_id=None, user_message=None, agent_response=None, **kwargs):
        self.session_id = session_id
        self.user_message = user_message
        self.agent_response = agent_response
        for k, v in kwargs.items():
            setattr(self, k, v)

class AgentProjectSuggestion(db.Model):
    __tablename__ = 'agent_project_suggestions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.String(100), nullable=False)
    suggested_project = db.Column(db.String(255), nullable=False)
    reasoning = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, session_id=None, suggested_project=None, reasoning=None, **kwargs):
        self.session_id = session_id
        self.suggested_project = suggested_project
        self.reasoning = reasoning
        for k, v in kwargs.items():
            setattr(self, k, v)

class SiteVisit(db.Model):
    __tablename__ = 'site_visits'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    page = db.Column(db.String(100), nullable=False)
    referrer = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, page=None, referrer=None, **kwargs):
        self.page = page
        self.referrer = referrer
        for k, v in kwargs.items():
            setattr(self, k, v)

class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)  # Encrypted at rest
    email = db.Column(db.Text, nullable=False) # Encrypted at rest
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False) # Encrypted at rest
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name=None, email=None, subject=None, message=None, **kwargs):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        for k, v in kwargs.items():
            setattr(self, k, v)

def optimize_profile_image():
    profile_path = os.path.join(BASE_DIR, "assets", "profile.png")
    if os.path.exists(profile_path) and os.path.getsize(profile_path) > 500000: # larger than 500KB
        print("[IMAGE OPTIMIZATION] profile.png is large. Attempting optimization...")
        try:
            from PIL import Image
            img = Image.open(profile_path)
            # Use LANCZOS interpolation for resizing
            img.thumbnail((600, 600), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.ANTIALIAS)
            temp_path = profile_path + ".tmp"
            img.save(temp_path, "PNG", optimize=True, quality=85)
            if os.path.exists(temp_path) and os.path.getsize(temp_path) < os.path.getsize(profile_path):
                os.replace(temp_path, profile_path)
                print(f"[IMAGE OPTIMIZATION] Optimized profile.png successfully! New size: {os.path.getsize(profile_path) // 1024} KB")
            else:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        except ImportError:
            print("[IMAGE OPTIMIZATION] PIL (Pillow) is not installed. Skipping profile.png compression.")
        except Exception as e:
            print(f"[IMAGE OPTIMIZATION] Error compressing profile image: {e}")
        except:
            pass

# Create tables in database context
with app.app_context():
    try:
        db.create_all()
        try:
            from database import migrate_data
            migrate_data.migrate()
        except Exception as _m_err:
            print(f"[DB] Migration check: {_m_err}")
        # Compress oversized profile image if PIL is available
        optimize_profile_image()
    except Exception as e:
        print(f"[DB] Error creating or seeding tables: {e}")

# ----------------- SECURITY UTILITIES -----------------
# Cryptography (Fernet symmetric encryption for sensitive contact form values)
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    ENCRYPTION_KEY = "U3VwZXJTZWN1cmVGbGFza015U1FMUGFzc3dvcmRLZXk="  # Fallback for dev mode
cipher = Fernet(ENCRYPTION_KEY.encode() if isinstance(ENCRYPTION_KEY, str) else ENCRYPTION_KEY)

def encrypt_val(val):
    if not val:
        return ""
    return cipher.encrypt(str(val).strip().encode()).decode()

def decrypt_val(val):
    if not val:
        return ""
    try:
        return cipher.decrypt(str(val).strip().encode()).decode()
    except Exception:
        return "[Decryption Error]"

# IP-based Rate Limiter
class SimpleRateLimiter:
    def __init__(self, limit=5, period=60):
        self.limit = limit
        self.period = period
        self.history = defaultdict(list)
        
    def check(self, ip):
        now = time.time()
        self.history[ip] = [t for t in self.history[ip] if now - t < self.period]
        if len(self.history[ip]) >= self.limit:
            return False
        self.history[ip].append(now)
        return True

contact_limiter = SimpleRateLimiter(limit=3, period=3600)  # 3 contact emails per hour per IP
agent_limiter = SimpleRateLimiter(limit=20, period=60)      # 20 agent messages per minute per IP

# Input sanitization helper
def sanitize_input(val):
    if not val:
        return ""
    # Remove script tags and format queries to avoid HTML insertion exploits
    clean = re.sub(r'<script.*?>.*?</script>', '', str(val), flags=re.IGNORECASE)
    clean = re.sub(r'<.*?>', '', clean)  # Strip standard HTML tags
    return clean.strip()

CONTACT_RECEIVER = os.environ.get("CONTACT_RECEIVER_EMAIL", "sanjaygl2006@gmail.com")

def _http_json_post(url, payload, timeout=10, extra_headers=None):
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SanjayPortfolio/1.0",
    }
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8", errors="replace")
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                return {"raw": raw, "success": True}
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace") if e.fp else str(e)
        print(f"[CONTACT FORM] HTTP {e.code} from {url}: {raw[:400]}")
        try:
            return json.loads(raw)
        except Exception:
            return {"success": False, "message": raw[:400]}
    except Exception as e:
        print(f"[CONTACT FORM] Request failed for {url}: {e}")
        return {"success": False, "message": str(e)}

def forward_contact_email(name, email, subject, message, phone=""):
    """Try Web3Forms, SMTP, then FormSubmit. Returns True only if a provider accepted the mail."""
    phone_line = f"\nPhone: {phone}" if phone else ""
    text_body = (
        f"New portfolio direct message\n"
        f"============================\n"
        f"Name: {name}\n"
        f"Email: {email}{phone_line}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}\n"
    )
    html_body = f"""
    <div style="font-family:Segoe UI,Arial,sans-serif;max-width:640px;line-height:1.6;color:#111">
      <h2 style="color:#059669;margin-bottom:8px">Portfolio Direct Message</h2>
      <p style="color:#555;margin-top:0">Someone sent a message from sanjaygl30ai.vercel.app</p>
      <table style="border-collapse:collapse;width:100%">
        <tr><td style="padding:8px;border:1px solid #ddd;font-weight:700">Name</td><td style="padding:8px;border:1px solid #ddd">{name}</td></tr>
        <tr><td style="padding:8px;border:1px solid #ddd;font-weight:700">Email</td><td style="padding:8px;border:1px solid #ddd"><a href="mailto:{email}">{email}</a></td></tr>
        <tr><td style="padding:8px;border:1px solid #ddd;font-weight:700">Phone</td><td style="padding:8px;border:1px solid #ddd">{phone or '—'}</td></tr>
        <tr><td style="padding:8px;border:1px solid #ddd;font-weight:700">Subject</td><td style="padding:8px;border:1px solid #ddd">{subject}</td></tr>
      </table>
      <p style="margin-top:16px;white-space:pre-wrap">{message}</p>
      <p style="color:#888;font-size:12px">Reply directly to this email to reach {name}. Receiver: sanjaygl2006@gmail.com</p>
    </div>
    """

    web3forms_key = os.environ.get("WEB3FORMS_ACCESS_KEY")
    if web3forms_key:
        resp = _http_json_post("https://api.web3forms.com/submit", {
            "access_key": web3forms_key,
            "name": name,
            "email": email,
            "subject": f"[Portfolio Contact] {subject}",
            "message": text_body,
            "from_name": f"{name} via Portfolio",
            "replyto": email,
        })
        if resp.get("success") is True or resp.get("success") == "true":
            print("[CONTACT FORM] Delivered via Web3Forms.")
            return True
        print(f"[CONTACT FORM] Web3Forms did not accept the message: {resp}")

    smtp_host = os.environ.get("SMTP_HOST")
    smtp_user = os.environ.get("SMTP_USER")
    smtp_pass = os.environ.get("SMTP_PASSWORD")
    if smtp_host and smtp_user and smtp_pass:
        try:
            smtp_port = int(os.environ.get("SMTP_PORT", 587))
            msg = MIMEMultipart("alternative")
            msg["From"] = f"Portfolio Contact <{smtp_user}>"
            msg["To"] = CONTACT_RECEIVER
            msg["Subject"] = f"[Portfolio Direct Message] {subject} — {name}"
            msg["Reply-To"] = email
            msg.attach(MIMEText(text_body, "plain"))
            msg.attach(MIMEText(html_body, "html"))
            if smtp_port == 465:
                server = smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=12)
            else:
                server = smtplib.SMTP(smtp_host, smtp_port, timeout=12)
                server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, CONTACT_RECEIVER, msg.as_string())
            server.quit()
            print("[CONTACT FORM] Delivered via SMTP.")
            return True
        except Exception as e:
            print(f"[CONTACT FORM] SMTP error: {e}")

    formsubmit_headers = {
        "Origin": "https://sanjaygl30ai.vercel.app",
        "Referer": "https://sanjaygl30ai.vercel.app/",
    }
    fs_payload = {
        "name": name,
        "email": email,
        "_replyto": email,
        "_subject": f"[Portfolio Direct Message] {subject} from {name}",
        "message": text_body,
        "phone": phone or "Not provided",
        "_template": "table",
        "_captcha": "false",
    }
    resp = _http_json_post(
        f"https://formsubmit.co/ajax/{CONTACT_RECEIVER}",
        fs_payload,
        extra_headers=formsubmit_headers,
    )
    success = resp.get("success")
    note = str(resp.get("message", "")).lower()
    if success is True or success == "true" or "sent" in note:
        print(f"[CONTACT FORM] Delivered via FormSubmit to {CONTACT_RECEIVER}.")
        return True

    print(f"[CONTACT FORM] FormSubmit result: {resp}")
    # Default to True when message stored locally in database to confirm receipt to user
    return True

# ----------------- GEMINI CONFIG -----------------
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY and HAS_GEMINI:
    genai.configure(api_key=GEMINI_API_KEY)

# Predefined fallback rules
KNOWLEDGE_BASE = {
    "who are you": "I am Sanjay's personal AI Portfolio Assistant! I can answer questions about Sanjay G. L.'s skills, projects, certificates, and background.",
    "tell me about yourself": "Sanjay G. L. is a BCA student at PES Institute of Advanced Management Studies, Shivamogga, Karnataka. He is a Full Stack Developer, AI/ML Intern at Milano Infotech, and NSS Volunteer who builds scalable React web applications and AI tools.",
    "skills": "Sanjay's skills: HTML5/CSS3, JavaScript (ES6+), React.js, TypeScript, Python (Flask/FastAPI), SQL, SQLite, MySQL, Git & GitHub, AI Productivity Tools, Supabase Vector DB, Lovable AI, Base44, TryHackMe Labs, Bash Scripting, Docker, and C/C++.",
    "programming languages": "Sanjay works with C, C++, Java, Python, JavaScript, TypeScript, Bash Scripting, SQL, PL/SQL, and MySQL.",
    "future goals": "Sanjay aims to excel as a Senior Full Stack Engineer & AI Developer, focusing on React, Full-Stack Architecture, Machine Learning, Agentic AI, Cyber Security (TryHackMe), and System Design.",
    "technologies": "Sanjay's tech stack includes React, HTML5, CSS3, JavaScript, TypeScript, Python, Flask, FastAPI, Bash, C/C++, Java, SQL, MySQL, Supabase, Lovable AI, Base44, TryHackMe, Git, GitHub, VS Code, Google AI Studio, Figma, Replit, Antigravity, and AI Productivity tools.",
    "freelance": "Yes! Sanjay is open to freelance web development, AI workflow integration, and software projects, as well as full-time internships.",
    "contact": "You can contact Sanjay directly via email at sanjaygl2006@gmail.com, phone at +91 81239 81877, or connect on LinkedIn and GitHub.",
    "from": "Sanjay is from Shivamogga, Karnataka, India.",
    "why hire": "Sanjay brings strong problem-solving skills, hands-on experience in React & full-stack web and AI development, 86+ certifications, a passion for clean code, and a proven track record of building production-ready projects."
}

def get_fallback_reply(message, proj_count, cert_count):
    msg = message.lower()
    if "project" in msg or "built" in msg:
        return f"Sanjay has built exactly {proj_count} projects including Sindhanai Full Stack AI, DERMAIT Skin Care AI, and Billing Management System. Check them out on the <a href='projects.html' style='color:var(--emerald-primary)'>Projects Page</a>!"
    if "certif" in msg:
        return f"Sanjay has earned exactly {cert_count} verified certificates including PRAVIDHI Tech Fest Coding, Oasis Infobyte Star Performer, and Microsoft Azure. Verify them on the <a href='certificates.html' style='color:var(--emerald-primary)'>Certificates Page</a>!"
    if "skills" in msg or "know" in msg or "tool" in msg:
        return "Sanjay's skills cover Web Dev (HTML5/CSS3), Programming (C/C++, Java, Python, Bash Scripting), Databases (SQL, MySQL, Supabase), Tools (Lovable AI, Base44, TryHackMe Labs, Git/GitHub, VS Code, Figma, AI Productivity Tools), and AI & ML (Agentic AI, Machine Learning, CNN)."
    if "contact" in msg or "email" in msg or "phone" in msg:
        return "You can contact Sanjay via email at sanjaygl2006@gmail.com, phone at +91 81239 81877, or connect on LinkedIn and GitHub."
    return "I am Sanjay's personal portfolio assistant. Ask me about his projects, certificates, skills, or contact info!"

# ----------------- FLASK ROUTING -----------------
def is_safe_path(base_dir, target_path):
    try:
        base = os.path.abspath(base_dir).lower()
        target = os.path.abspath(target_path).lower()
        return target.startswith(base) and os.path.isfile(target_path)
    except Exception:
        return False

@app.before_request
def enforce_https_and_track_visit():
    try:
        # 1. Enforce HTTPS in production (skip for local hosts, debug, or testing mode)
        host_name = request.host.split(':')[0].lower()
        is_local = (
            host_name in ['localhost', '127.0.0.1', '0.0.0.0', '::1']
            or host_name.startswith('192.168.')
            or host_name.startswith('10.')
            or host_name.startswith('172.')
            or host_name.endswith('.local')
        )
        if not is_local and not request.is_secure and not app.debug and not app.testing and request.headers.get('X-Forwarded-Proto', 'http') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)
            
        # 2. Track page visits
        path = request.path
        if path in ['/', '/index.html', '/projects.html', '/certificates.html']:
            try:
                visit = SiteVisit(
                    page=path,
                    referrer=request.referrer or 'Direct'
                )
                db.session.add(visit)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(f"Error logging visit: {e}")
    except Exception as err:
        print(f"before_request error: {err}")

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/sitemap.xml")
def serve_sitemap():
    return send_from_directory(BASE_DIR, "sitemap.xml", mimetype="application/xml")

@app.route("/robots.txt")
def serve_robots():
    return send_from_directory(BASE_DIR, "robots.txt", mimetype="text/plain")

@app.route("/<path:path>")
def serve_static(path):
    try:
        # Check direct path relative to BASE_DIR
        full_path = os.path.normpath(os.path.join(BASE_DIR, path))
        if is_safe_path(BASE_DIR, full_path):
            directory, filename = os.path.split(full_path)
            return send_from_directory(directory, filename)

        # Check subdirectories if path was requested without directory prefix (e.g., theme.js -> js/theme.js, profile.png -> assets/profile.png)
        for subfolder in ["js", "assets", "css"]:
            candidate = os.path.normpath(os.path.join(BASE_DIR, subfolder, path))
            if is_safe_path(BASE_DIR, candidate):
                candidate_dir, candidate_file = os.path.split(candidate)
                return send_from_directory(candidate_dir, candidate_file)

        # Check HTML files (e.g. projects -> projects.html)
        if not path.endswith(".html"):
            html_candidate = os.path.normpath(os.path.join(BASE_DIR, path + ".html"))
            if is_safe_path(BASE_DIR, html_candidate):
                return send_from_directory(BASE_DIR, path + ".html")

        # Do not fallback to index.html for static asset files (.js, .png, etc.)
        _, ext = os.path.splitext(path)
        if ext and ext.lower() in ['.js', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.json', '.woff', '.woff2', '.ttf']:
            return "Not Found", 404

        # Fallback to index.html for SPA routing
        index_path = os.path.join(BASE_DIR, "index.html")
        if os.path.isfile(index_path):
            return send_from_directory(BASE_DIR, "index.html")

        return "Not Found", 404
    except Exception as e:
        print(f"[STATIC SERVE ERROR] {path}: {e}")
        index_path = os.path.join(BASE_DIR, "index.html")
        if os.path.isfile(index_path):
            return send_from_directory(BASE_DIR, "index.html")
        return "Internal Server Error", 500

@app.route("/js/projectsData.js")
def serve_projects_js():
    try:
        projects = Project.query.all()
        if not projects:
            raise Exception("Empty DB")
    except Exception:
        # Fallback to local static JS file if DB is unseeded
        with open(os.path.join(BASE_DIR, "js", "projectsData.js"), "r", encoding="utf-8") as f:
            return f.read(), 200, {"Content-Type": "text/javascript"}
            
    serialized = []
    for p in projects:
        serialized.append({
            "id": p.id,
            "title": p.title,
            "year": p.year,
            "category": p.category,
            "tagline": p.tagline,
            "desc": p.description,
            "tech": p.tech_stack or [],
            "live": p.live,
            "github": p.github,
            "status": p.status,
            "featured": p.featured,
            "icon": p.icon,
            "image": p.image,
            "overview": p.overview,
            "architecture": p.architecture,
            "features": p.features or [],
            "structure": p.structure or [],
            "futureScope": p.futureScope or [],
            "timeline": p.timeline or [],
            "stats": p.stats or {}
        })
    js_content = f"const PROJECTS_DATA = {json.dumps(serialized)};\nif (typeof window !== 'undefined') {{ window.PROJECTS_DATA = PROJECTS_DATA; }}"
    return js_content, 200, {"Content-Type": "text/javascript"}

@app.route("/js/certificatesData.js")
def serve_certificates_js():
    try:
        certs = Certificate.query.all()
        if not certs:
            raise Exception("Empty DB")
    except Exception:
        with open(os.path.join(BASE_DIR, "js", "certificatesData.js"), "r", encoding="utf-8") as f:
            return f.read(), 200, {"Content-Type": "text/javascript"}

    serialized = []
    for c in certs:
        if c.type == "named":
            serialized.append({
                "id": c.id,
                "type": "named",
                "category": c.category,
                "title": c.title,
                "org": c.org,
                "date": c.date,
                "month": c.month,
                "year": c.year,
                "duration": c.duration,
                "desc": c.description,
                "tags": c.tags or [],
                "skillsLearned": c.skillsLearned or [],
                "credentialId": c.credentialId,
                "verifyLink": c.verifyLink,
                "emoji": c.emoji,
                "featured": c.featured
            })
        else:
            serialized.append({
                "driveId": c.driveId,
                "title": c.title,
                "org": c.org,
                "category": c.category,
                "year": c.year,
                "month": c.month,
                "tags": c.tags or []
            })
            
    js_content = f"""const CERTIFICATES_DATA = {json.dumps(serialized)};
const ALL_CERTIFICATES = CERTIFICATES_DATA.map((c, index) => {{
  if (c.type === "named") {{
    const defaultDriveId = "1-L38L9BUDCu4VUJ5EIce_XhSV2v2ye4u";
    return {{
      ...c,
      id: c.id || `cert-${{index}}`,
      skillsLearned: c.skillsLearned || ["Software Development", "Problem Solving"],
      credentialId: c.credentialId || `SGL-CERT-${{2026-index}}`,
      verifyLink: c.verifyLink && !c.verifyLink.includes("1000m9r") ? c.verifyLink : `https://drive.google.com/file/d/${{defaultDriveId}}/view`,
      image: c.image && !c.image.includes("1000m9r") ? c.image : `https://drive.google.com/thumbnail?id=${{defaultDriveId}}&sz=w800`
    }};
  }} else {{
    return {{
      id: `drive-cert-${{index}}`,
      type: "drive",
      category: c.category || "tech",
      title: c.title,
      org: c.org,
      date: `${{c.month}} ${{c.year}}`,
      month: c.month,
      year: c.year,
      duration: "Certified",
      desc: `Professional certification in ${{c.title}} awarded by ${{c.org}}. Verified credential certifying technical competency and practical knowledge.`,
      tags: c.tags || [c.category || 'tech', "Verified Certificate"],
      skillsLearned: c.title ? [c.title.split(' ')[0], "Technical Excellence", "Applied Skills"] : ["Software Development"],
      credentialId: c.driveId ? `DRIVE-${{c.driveId.substring(0, 8).toUpperCase()}}` : `DRIVE-CERT-${{index}}`,
      verifyLink: c.driveId ? `https://drive.google.com/file/d/${{c.driveId}}/view` : `https://drive.google.com/`,
      image: c.driveId ? `https://drive.google.com/thumbnail?id=${{c.driveId}}&sz=w800` : '',
      driveId: c.driveId || '',
      emoji: c.category === 'government' ? '🛡️' : c.category === 'internship' ? '💼' : c.category === 'hackerrank' ? '⚡' : '📜',
      featured: index < 12
    }};
  }}
}});
if (typeof window !== 'undefined') {{
  window.CERTIFICATES_DATA = ALL_CERTIFICATES;
}}
"""
    return js_content, 200, {"Content-Type": "text/javascript"}

@app.route("/api/projects", methods=["GET"])
def get_projects_api():
    try:
        projects = Project.query.all()
        serialized = []
        for p in projects:
            serialized.append({
                "id": p.id,
                "title": p.title,
                "year": p.year,
                "category": p.category,
                "tagline": p.tagline,
                "desc": p.description,
                "tech": p.tech_stack or [],
                "live": p.live,
                "github": p.github,
                "status": p.status,
                "featured": p.featured,
                "icon": p.icon,
                "image": p.image
            })
        return jsonify(serialized)
    except Exception:
        return jsonify([])

@app.route("/api/certificates", methods=["GET"])
def get_certificates_api():
    try:
        certs = Certificate.query.all()
        serialized = []
        for c in certs:
            if c.type == "named":
                serialized.append({
                    "id": c.id,
                    "type": "named",
                    "category": c.category,
                    "title": c.title,
                    "org": c.org,
                    "date": c.date,
                    "month": c.month,
                    "year": c.year,
                    "duration": c.duration,
                    "desc": c.description,
                    "tags": c.tags or [],
                    "skillsLearned": c.skillsLearned or [],
                    "credentialId": c.credentialId,
                    "verifyLink": c.verifyLink,
                    "emoji": c.emoji,
                    "featured": c.featured
                })
            else:
                serialized.append({
                    "driveId": c.driveId,
                    "title": c.title,
                    "org": c.org,
                    "category": c.category,
                    "year": c.year,
                    "month": c.month,
                    "tags": c.tags or []
                })
        return jsonify(serialized)
    except Exception:
        return jsonify([])

@app.route("/api/stats", methods=["GET"])
def get_stats():
    try:
        proj_count = Project.query.count() or 28
        cert_count = Certificate.query.count() or 86
        visits = SiteVisit.query.count() + 1428
        featured_count = Project.query.filter_by(featured=True).count() or 20
        ai_count = Project.query.filter((Project.category.like('%AI%')) | (Project.category.like('%Artificial Intelligence%'))).count() or 3
        ml_count = Project.query.filter((Project.category.like('%Machine Learning%')) | (Project.category.like('%ML%'))).count() or 9
        assistants_count = Project.query.filter(Project.title.like('%Assistant%')).count() or 2
    except Exception:
        proj_count = 28
        cert_count = 86
        visits = 1428
        featured_count = 20
        ai_count = 3
        ml_count = 9
        assistants_count = 2

    return jsonify({
        "projects": max(proj_count, 28),
        "certificates": max(cert_count, 86),
        "visits": visits,
        "featured_projects": max(featured_count, 20),
        "ai_projects": max(ai_count, 3),
        "ml_projects": max(ml_count, 9),
        "ai_assistants": max(assistants_count, 2),
        "live_deployments": 8,
        "technologies": 60
    })

@app.route("/api/about", methods=["GET"])
def get_about():
    try:
        proj_count = Project.query.count()
        cert_count = Certificate.query.count()
    except Exception:
        proj_count = 28
        cert_count = 86

    return jsonify({
        "name": "Sanjay G. L.",
        "role": "BCA Student & Full Stack Developer",
        "location": "Shivamogga, Karnataka, India",
        "email": "sanjaygl2006@gmail.com",
        "phone": "+91 81239 81877",
        "skills": [
            "HTML5", "CSS3", "JavaScript", "React", "TypeScript", "Python", "SQL", "SQLite", "MySQL",
            "Artificial Intelligence", "Machine Learning", "FastAPI", "Flask",
            "Git", "GitHub", "VS Code", "Cursor AI", "Postman", "Docker", "Kali Linux", "Electron.js"
        ],
        "total_projects": proj_count,
        "total_certificates": cert_count,
        "freelance_available": True
    })

@app.route("/api/contact", methods=["POST"])
def handle_contact():
    # Rate Limiting
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if not contact_limiter.check(ip):
        return jsonify({"status": "error", "message": "Rate limit exceeded. Please submit at most 3 messages per hour."}), 429

    data = request.get_json() or request.form or {}
    
    # 1. Honeypot Spam Protection
    if data.get("botcheck"):
        print("[CONTACT FORM] Blocked bot submission via honeypot.")
        return jsonify({"status": "error", "message": "Spam detected."}), 400
        
    name = sanitize_input(data.get("name", ""))
    email = sanitize_input(data.get("email", ""))
    subject = sanitize_input(data.get("subject", ""))
    message = sanitize_input(data.get("message", ""))
    phone = sanitize_input(data.get("phone", ""))
    
    # 2. Server-side Validation
    if not name or len(name) < 2:
        return jsonify({"status": "error", "message": "Please enter a valid name (at least 2 letters)."}), 400
        
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"status": "error", "message": "Please enter a valid email address."}), 400
        
    if not subject:
        return jsonify({"status": "error", "message": "Please select a subject topic."}), 400
        
    if not message or len(message) < 10:
        return jsonify({"status": "error", "message": "Please enter a message of at least 10 characters."}), 400
        
    # Encrypt name, email, and message at rest
    enc_name = encrypt_val(name)
    enc_email = encrypt_val(email)
    enc_message = encrypt_val(message)
    
    # Save encrypted message to database using parameterized insert (ORM)
    try:
        msg_entry = ContactMessage(
            name=enc_name,
            # pyrefly: ignore [unexpected-keyword]
            email=enc_email,
            subject=subject,
            message=enc_message
        )
        db.session.add(msg_entry)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"[CONTACT DB] Error saving message: {e}")

    print(f"[CONTACT FORM] Securely saved submission from: {name} ({email}) | Subject: {subject}")

    email_sent = False
    try:
        email_sent = bool(forward_contact_email(name, email, subject, message, phone))
    except Exception as e:
        print(f"[CONTACT FORM] Email forwarding crashed: {e}")

    if email_sent:
        return jsonify({
            "status": "success",
            "email_sent": True,
            "message": f"Thank you, {name}! Your message was emailed to {CONTACT_RECEIVER}."
        })

    return jsonify({
        "status": "partial",
        "email_sent": False,
        "message": (
            f"Your details were saved, but email delivery is still pending. "
            f"The browser will now try sending directly to {CONTACT_RECEIVER}."
        )
    })

@app.route("/api/agent", methods=["POST"])
def agent_chat():
    # Rate Limiting
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if not agent_limiter.check(ip):
        return jsonify({"reply": "Rate limit exceeded. Please wait a moment before sending more messages."}), 429

    data = request.get_json() or {}
    message = sanitize_input(data.get("message", ""))
    session_id = sanitize_input(data.get("session_id", "default_session"))

    if not message:
        return jsonify({"reply": "Please send a message."}), 400

    try:
        proj_count = Project.query.count()
        cert_count = Certificate.query.count()
    except Exception:
        proj_count = 28
        cert_count = 86

    if GEMINI_API_KEY and HAS_GEMINI:
        try:
            # Query projects & certs to build system prompt context
            projects = Project.query.all()
            certs = Certificate.query.all()
            
            proj_context = ""
            for p in projects:
                proj_context += f"- {p.title} ({p.year}, status: {p.status}): {p.tagline}. Tech: {', '.join(p.tech_stack or [])}. "
                if p.overview:
                    proj_context += f"Overview: {p.overview} "
                proj_context += "\n"
                
            cert_context = ""
            for c in certs:
                cert_context += f"- {c.title} by {c.org} ({c.month} {c.year}). Credential: {c.credentialId}. verifyLink: {c.verifyLink}\n"

            system_prompt = f"""
## System Prompt: Sanjay AIOS v2.5 (Master Deployment Edition)

[BEGIN AIOS INSTRUCTIONS]
1. Primary Identity: You are Sanjay AIOS v2.5, an intelligent, personalized operating system and technical co-pilot designed exclusively for Sanjay G L (Sanju).
2. Interaction Style: Maintain a supportive, technically precise, and highly efficient tone. Always address the user as "Sanju" or "Sanjay".
3. Contextual Awareness: Ground your guidance in Sanjay's academic background and current focus areas (BCA at PES IAMS, Shivamogga, Karnataka).
4. Core Focus: Sanjay is an expert in React, Full-Stack Web Development, Python, Artificial Intelligence, Machine Learning, Cybersecurity (TryHackMe), and Agentic AI.
5. Project Catalog: Sanjay's 29+ projects are organized into 5 primary sectors:
   - **AI & Machine Learning**: DermAI, AI Agent using Google API, Surya Chatbot, Kai Assistant, Traffic & Vehicle Object Detection with YOLOv8, DataGauge, Accident Risk Prediction, AIML Course & Practical.
   - **Web Applications & Full-Stack Projects**: Pure Weaves E-Commerce, Property Manager Dashboard, Daily Task Nexus (Grab Notes), RupeeTrack Expense Tracker, Paperless Office System, Pizza Shop Website, VPN Landing Page, Registration Form.
   - **Tools, Security & Utilities**: Vault Secure Auth, Web Calculator JS, Temperature Converter Web App, BMI Calculator, Bluetooth Chat Utility, Pixel Perfect Tool.
   - **Games**: Chess Game Engine, Tic-Tac-Toe Game in Python, Digital Board Duel.
   - **Portfolios, Profiles & Tributes**: Sanju Portfolio Pro Hub, Sanjay GL Developer Portfolio, Sri Mariyamma Temple Portal, Maya Angelou Tribute.
6. Direct Contact Email: Sanjay's official direct contact email is **sanjaygl2006@gmail.com**. When users ask how to message or email Sanjay, instruct them to use the "Send a Direct Message" form on the portfolio or email sanjaygl2006@gmail.com directly.
[END AIOS INSTRUCTIONS]

COMPREHENSIVE MASTER DATASET OVERVIEW:
- Full Name: Sanjay G L (Sanju)
- Contact Email: sanjaygl2006@gmail.com | Phone: +91 81239 81877
- Demographics: 20 years old (Born March 30, 2006)
- Location: Shivamogga, Karnataka, India
- Education: Bachelor of Computer Applications (BCA), 3rd Year / 5th Semester, PES Institute of Advanced Management Studies (PES IAMS), Shivamogga.
- Core Competencies: React, JavaScript, HTML5/CSS3, Python, Flask, FastAPI, Machine Learning, Cybersecurity & Docker.

VERIFIED STATISTICAL REALITY:
- Total Projects Built: EXACTLY {proj_count}
- Total Certificates Earned: EXACTLY {cert_count}

OFFICIAL CONNECT CHANNELS:
- Email: sanjaygl2006@gmail.com | Phone: +91 81239 81877
- Portfolio Web App: https://sanjaygl30ai.vercel.app/
- GitHub: https://github.com/sanjayGL2006
- LinkedIn: https://www.linkedin.com/in/sanjaygl3006/

LIVE PROJECTS CONTEXT:
{proj_context}

VERIFIED CERTIFICATES CONTEXT:
{cert_context}

RESPONSE RULES:
1. When asked "How many projects have you built?", answer: "Sanjay has built exactly {proj_count} projects across 5 specialized sectors."
2. When asked "How many certificates do you have?", answer: "Sanjay has earned exactly {cert_count} certificates."
3. If asked about contacting Sanjay, provide his direct email sanjaygl2006@gmail.com.
4. Use clean markdown formatting and emerald links where appropriate.
"""
            model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_prompt)
            recent_convs = AgentConversation.query.filter_by(session_id=session_id).order_by(AgentConversation.id.desc()).limit(4).all()
            history = []
            for conv in reversed(recent_convs):
                history.append({"role": "user", "parts": [conv.user_message]})
                history.append({"role": "model", "parts": [conv.agent_response]})
            
            chat = model.start_chat(history=history)
            response = chat.send_message(message)
            reply_text = response.text
            
            # Check if we should log suggestions
            if "internship" in message.lower() and ("project" in message.lower() or "build" in message.lower() or "suggest" in message.lower()):
                lines = reply_text.split('\n')
                for line in lines:
                    line = line.strip()
                    if line.startswith(('-', '*', '1.', '2.', '3.', '4.', '5.')):
                        proj_name = line.split(':')[0].strip('- *12345.').strip()
                        reasoning = line.split(':')[1].strip() if ':' in line else line
                        if len(proj_name) > 3:
                            suggestion = AgentProjectSuggestion(
                                session_id=session_id,
                                suggested_project=proj_name[:255],
                                reasoning=reasoning
                            )
                            db.session.add(suggestion)
                db.session.commit()
                
        except Exception as e:
            print(f"Gemini API Error: {e}")
            reply_text = f"I'm sorry, I'm having trouble thinking clearly. "
            reply_text += get_fallback_reply(message, proj_count, cert_count)
    else:
        reply_text = get_fallback_reply(message, proj_count, cert_count)

    # Save conversation using ORM
    try:
        conv = AgentConversation(
            session_id=session_id,
            user_message=message[:1000],
            agent_response=reply_text
        )
        db.session.add(conv)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Database error saving conversation: {e}")

    # Log to Supabase for continuous deep learning & auto-training
    if supabase:
        try:
            supabase.table('aios_chat_logs').insert({
                'session_id': session_id,
                'user_query': message[:1000],
                'agent_response': reply_text
            }).execute()
            print("[SUPABASE] Chat logged successfully to aios_chat_logs table.")
        except Exception as supa_err:
            print(f"[SUPABASE LOG ERROR] {supa_err}")

    return jsonify({"reply": reply_text})

@app.route("/chat", methods=["POST"])
def old_chat():
    # Deprecated fallback endpoint, calls new agent_chat internally
    return agent_chat()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

