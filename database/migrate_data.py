import os
import re
import json
import subprocess
# pyrefly: ignore [missing-import]
import pymysql
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

def load_js_data(file_path, var_name):
    """Safely loads JS data file into Python list using Node.js evaluation."""
    abs_path = os.path.abspath(file_path)
    if not os.path.exists(abs_path):
        return []
    
    # 1. Try evaluating with Node.js first
    try:
        cmd = [
            "node", "-e",
            f"const fs = require('fs'); const window = {{}}; const code = fs.readFileSync({json.dumps(abs_path)}, 'utf8'); eval(code); console.log(JSON.stringify(window.{var_name} || {var_name}));"
        ]
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, timeout=5).decode("utf-8")
        parsed = json.loads(out)
        if isinstance(parsed, list):
            return parsed
    except Exception as e:
        print(f"[MIGRATION] Node.js evaluation notice for {file_path}: {e}")

    # 2. Fallback to Python AST literal evaluation
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r'const\s+' + var_name + r'\s*=\s*(\[[\s\S]*?\])\s*;', content)
        if match:
            js_str = match.group(1)
            js_str = re.sub(r'//.*', '', js_str)
            js_str = re.sub(r'\btrue\b', 'True', js_str)
            js_str = re.sub(r'\bfalse\b', 'False', js_str)
            js_str = re.sub(r'\bnull\b', 'None', js_str)
            js_str = re.sub(r'(?<=[{\s,])([a-zA-Z_]\w*)\s*:', r'"\1":', js_str)
            js_str = re.sub(r',\s*([\]\}])', r'\1', js_str)
            import ast
            return ast.literal_eval(js_str)
    except Exception as err:
        print(f"[MIGRATION] Python fallback parse notice: {err}")
    return []

def migrate():
    # Database connection URL setup
    db_url = os.environ.get("DATABASE_URL")
    db_host = os.environ.get("DB_HOST", "localhost")
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")
    db_port = int(os.environ.get("DB_PORT", "3306"))
    
    use_sqlite = True
    if db_url and db_url.startswith("mysql"):
        use_sqlite = False
    elif db_host and db_user and db_name:
        use_sqlite = False
        
    if use_sqlite:
        import sqlite3
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portfolio.db")
        print(f"[MIGRATION] Connecting to local SQLite database {db_path}...")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    else:
        print(f"[MIGRATION] Connecting to MySQL database at {db_host}:{db_port}...")
        ssl_ca = os.environ.get("DB_SSL_CA")
        ssl_args = None
        if ssl_ca:
            ssl_args = {"ssl": {"ca": ssl_ca}}
        elif os.environ.get("DB_SSL_REQUIRE", "false").lower() == "true":
            ssl_args = {"ssl": {"ssl_mode": "REQUIRED"}}
            
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name,
            port=db_port,
            **ssl_args if ssl_args else {}
        )
        cursor = conn.cursor()

    # 1. Migrate Projects
    projects_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "js", "projectsData.js")
    projects = load_js_data(projects_file, "PROJECTS_DATA")
    if projects:
        print(f"[MIGRATION] Loaded {len(projects)} projects from projectsData.js. Migrating...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                year INT,
                category VARCHAR(100),
                tagline TEXT,
                description TEXT,
                tech_stack JSON,
                live VARCHAR(255),
                github VARCHAR(255),
                status VARCHAR(50),
                featured BOOLEAN,
                icon VARCHAR(100),
                image VARCHAR(255),
                overview TEXT,
                architecture TEXT,
                features JSON,
                structure JSON,
                futureScope JSON,
                timeline JSON,
                stats JSON
            )
        """)
        
        cursor.execute("DELETE FROM projects")
        
        for p in projects:
            sql = """
                INSERT INTO projects (
                    id, title, year, category, tagline, description, tech_stack, live, github, status, featured, icon, image, overview, architecture, features, structure, futureScope, timeline, stats
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """ if not use_sqlite else """
                INSERT INTO projects (
                    id, title, year, category, tagline, description, tech_stack, live, github, status, featured, icon, image, overview, architecture, features, structure, futureScope, timeline, stats
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            cursor.execute(sql, (
                p.get('id'),
                p.get('title'),
                p.get('year'),
                p.get('category'),
                p.get('tagline'),
                p.get('desc') or p.get('description'),
                json.dumps(p.get('tech', [])),
                p.get('live', ''),
                p.get('github', ''),
                p.get('status', 'Completed'),
                p.get('featured', False),
                p.get('icon', 'fa-code'),
                p.get('image', ''),
                p.get('overview', ''),
                p.get('architecture', ''),
                json.dumps(p.get('features', [])),
                json.dumps(p.get('structure', [])),
                json.dumps(p.get('futureScope', [])),
                json.dumps(p.get('timeline', [])),
                json.dumps(p.get('stats', {}))
            ))

    # 2. Migrate Certificates
    certs_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "js", "certificatesData.js")
    certificates = load_js_data(certs_file, "CERTIFICATES_DATA") or load_js_data(certs_file, "ALL_CERTIFICATES")
    if certificates:
        print(f"[MIGRATION] Loaded {len(certificates)} certificates from certificatesData.js. Migrating...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certificates (
                id VARCHAR(100) PRIMARY KEY,
                type VARCHAR(50),
                category VARCHAR(100),
                title VARCHAR(255) NOT NULL,
                org VARCHAR(255),
                date VARCHAR(100),
                month VARCHAR(50),
                year INT,
                duration VARCHAR(100),
                description TEXT,
                tags JSON,
                skillsLearned JSON,
                credentialId VARCHAR(100),
                verifyLink VARCHAR(500),
                image VARCHAR(500),
                driveId VARCHAR(100),
                emoji VARCHAR(50),
                featured BOOLEAN
            )
        """)

        cursor.execute("DELETE FROM certificates")

        for idx, c in enumerate(certificates):
            sql = """
                INSERT INTO certificates (
                    id, type, category, title, org, date, month, year, duration, description, tags, skillsLearned, credentialId, verifyLink, image, driveId, emoji, featured
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """ if not use_sqlite else """
                INSERT INTO certificates (
                    id, type, category, title, org, date, month, year, duration, description, tags, skillsLearned, credentialId, verifyLink, image, driveId, emoji, featured
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            cert_id = c.get('id') or (f"drive-{c.get('driveId')}" if c.get('driveId') else f"cert-{idx}")
            cursor.execute(sql, (
                str(cert_id),
                c.get('type', 'named' if 'credentialId' in c else 'drive'),
                c.get('category', 'tech'),
                c.get('title', 'Certificate'),
                c.get('org', 'Issuer'),
                c.get('date', f"{c.get('month', '')} {c.get('year', '')}".strip()),
                c.get('month', ''),
                c.get('year', 2025),
                c.get('duration', 'Certified'),
                c.get('desc') or c.get('description', ''),
                json.dumps(c.get('tags', [])),
                json.dumps(c.get('skillsLearned', [])),
                c.get('credentialId', ''),
                c.get('verifyLink', ''),
                c.get('image', ''),
                c.get('driveId', ''),
                c.get('emoji', '📜'),
                c.get('featured', True)
            ))

    conn.commit()
    cursor.close()
    conn.close()
    print("[MIGRATION] Migration successfully complete!")

if __name__ == "__main__":
    migrate()
