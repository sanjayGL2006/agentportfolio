import os
import re
import json
import pymysql
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

def clean_js_object(js_str):
    # Strip comments
    js_str = re.sub(r'//.*', '', js_str)
    # Quote keys
    json_str = re.sub(r'(\w+):', r'"\1":', js_str)
    # Replace single quotes with double quotes
    json_str = re.sub(r"'([^'\\]*(?:\\.[^'\\]*)*)'", r'"\1"', json_str)
    # Remove trailing commas
    json_str = re.sub(r',(\s*[\]\}])', r'\1', json_str)
    # Normalize true/false/null
    json_str = json_str.replace("true", "true").replace("false", "false")
    return json_str

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
        print("[MIGRATION] Connecting to local SQLite database portfolio.db...")
        conn = sqlite3.connect("portfolio.db")
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
    projects_file = r"js/projectsData.js"
    if os.path.exists(projects_file):
        with open(projects_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        array_match = re.search(r'const PROJECTS_DATA\s*=\s*(\[[\s\S]*\]);', content)
        if array_match:
            try:
                js_array = array_match.group(1)
                json_str = clean_js_object(js_array)
                projects = json.loads(json_str)
                
                print(f"[MIGRATION] Loaded {len(projects)} projects from projectsData.js. Migrating...")
                
                # Check table exists (create if not)
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
                
                # Clear existing projects to rebuild and sync updates from js file
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
                        p.get('desc'),
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
                conn.commit()
                print("[MIGRATION] Projects migration completed successfully.")
            except Exception as e:
                print(f"[MIGRATION] Error migrating projects: {e}")

    # 2. Migrate Certificates
    certs_file = r"js/certificatesData.js"
    if os.path.exists(certs_file):
        with open(certs_file, "r", encoding="utf-8") as f:
            content = f.read()

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

        # Extract and parse named certs
        named_blocks = re.findall(r'\{\s*id:\s*"cert-named-\d+"[\s\S]*?\}\s*(?=,|\s*\])', content)
        print(f"[MIGRATION] Found {len(named_blocks)} named certificates. Migrating...")
        for block in named_blocks:
            try:
                json_str = clean_js_object(block)
                c = json.loads(json_str)
                
                sql = """
                    INSERT INTO certificates (
                        id, type, category, title, org, date, month, year, duration, description, tags, skillsLearned, credentialId, verifyLink, image, driveId, emoji, featured
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """ if not use_sqlite else """
                    INSERT INTO certificates (
                        id, type, category, title, org, date, month, year, duration, description, tags, skillsLearned, credentialId, verifyLink, image, driveId, emoji, featured
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """

                cursor.execute(sql, (
                    c.get('id'),
                    'named',
                    c.get('category'),
                    c.get('title'),
                    c.get('org'),
                    c.get('date'),
                    c.get('month'),
                    c.get('year'),
                    c.get('duration'),
                    c.get('desc'),
                    json.dumps(c.get('tags', [])),
                    json.dumps(c.get('skillsLearned', [])),
                    c.get('credentialId'),
                    c.get('verifyLink'),
                    c.get('image', ''),
                    c.get('driveId', ''),
                    c.get('emoji', '📜'),
                    c.get('featured', True)
                ))
            except Exception as e:
                print(f"[MIGRATION] Error parsing named certificate: {e}")

        # Extract and parse drive certs
        drive_blocks = re.findall(r'\{\s*driveId:\s*\'[^\']+\'[\s\S]*?\}', content)
        print(f"[MIGRATION] Found {len(drive_blocks)} drive certificates. Migrating...")
        for idx, block in enumerate(drive_blocks):
            try:
                json_str = clean_js_object(block)
                c = json.loads(json_str)
                
                c_id = f"drive-cert-{idx}"
                sql = """
                    INSERT INTO certificates (
                        id, type, category, title, org, date, month, year, duration, description, tags, skillsLearned, credentialId, verifyLink, image, driveId, emoji, featured
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """ if not use_sqlite else """
                    INSERT INTO certificates (
                        id, type, category, title, org, date, month, year, duration, description, tags, skillsLearned, credentialId, verifyLink, image, driveId, emoji, featured
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """

                # Replicate normalization mappings inside the DB
                cat = c.get('category', 'tech')
                title = c.get('title', '')
                org = c.get('org', '')
                month = c.get('month', 'September')
                year = c.get('year', 2025)
                did = c.get('driveId', '')

                cursor.execute(sql, (
                    c_id,
                    'drive',
                    cat,
                    title,
                    org,
                    f"{month} {year}",
                    month,
                    year,
                    "Certified",
                    f"Professional certification in {title} awarded by {org}. Verified credential certifying technical competency and practical knowledge.",
                    json.dumps(c.get('tags', [cat, "Verified Certificate"])),
                    json.dumps([title.split(' ')[0], "Technical Excellence", "Applied Skills"]),
                    f"DRIVE-{did[:8].upper()}" if did else f"DRIVE-CERT-{idx}",
                    f"https://drive.google.com/file/d/{did}/view" if did else "https://drive.google.com/",
                    f"https://drive.google.com/thumbnail?id={did}&sz=w800" if did else "",
                    did,
                    '🛡️' if cat == 'government' else '💼' if cat == 'internship' else '⚡' if cat == 'hackerrank' else '📜',
                    idx < 12
                ))
            except Exception as e:
                print(f"[MIGRATION] Error parsing drive certificate: {e}")

        conn.commit()
        print("[MIGRATION] Certificates migration completed successfully.")

    # 3. Create logs/visits tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agent_conversations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            session_id VARCHAR(100) NOT NULL,
            user_message TEXT NOT NULL,
            agent_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """ if not use_sqlite else """
        CREATE TABLE IF NOT EXISTS agent_conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id VARCHAR(100) NOT NULL,
            user_message TEXT NOT NULL,
            agent_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agent_project_suggestions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            session_id VARCHAR(100) NOT NULL,
            suggested_project VARCHAR(255) NOT NULL,
            reasoning TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """ if not use_sqlite else """
        CREATE TABLE IF NOT EXISTS agent_project_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id VARCHAR(100) NOT NULL,
            suggested_project VARCHAR(255) NOT NULL,
            reasoning TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS site_visits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            page VARCHAR(100) NOT NULL,
            referrer VARCHAR(255),
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """ if not use_sqlite else """
        CREATE TABLE IF NOT EXISTS site_visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            page VARCHAR(100) NOT NULL,
            referrer VARCHAR(255),
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact_messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject VARCHAR(255) NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """ if not use_sqlite else """
        CREATE TABLE IF NOT EXISTS contact_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject VARCHAR(255) NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("[MIGRATION] Migration successfully complete!")

if __name__ == "__main__":
    migrate()
