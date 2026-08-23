import os
import sqlite3
import pymysql
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

# Read the decryption key from environment (use default fallback if in development)
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", "U3VwZXJTZWN1cmVGbGFza015U1FMUGFzc3dvcmRLZXk=")
cipher = Fernet(ENCRYPTION_KEY.encode() if isinstance(ENCRYPTION_KEY, str) else ENCRYPTION_KEY)

def decrypt_val(val):
    if not val:
        return ""
    try:
        return cipher.decrypt(str(val).strip().encode()).decode()
    except Exception:
        return "[Decryption Error]"

def get_connection():
    db_url = os.environ.get("DATABASE_URL")
    db_host = os.environ.get("DB_HOST")
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
        db_path = "portfolio.db"
        print(f"[DECRYPTOR] Connecting to local SQLite database {db_path}...")
        return sqlite3.connect(db_path), True
    else:
        print(f"[DECRYPTOR] Connecting to MySQL database at {db_host}:{db_port}...")
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
        return conn, False

def main():
    try:
        conn, is_sqlite = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, email, message, timestamp FROM contact_messages ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        
        print("\n" + "="*80)
        print(f"DECRYPTED CONTACT MESSAGES ({len(rows)} messages found)")
        print("="*80)
        
        for row in rows:
            msg_id, enc_name, enc_email, enc_message, timestamp = row
            name = decrypt_val(enc_name)
            email = decrypt_val(enc_email)
            message = decrypt_val(enc_message)
            
            print(f"ID        : {msg_id}")
            print(f"Timestamp : {timestamp}")
            print(f"Name      : {name}")
            print(f"Email     : {email}")
            print(f"Message   : {message}")
            print("-"*80)
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[DECRYPTOR] Error querying or decrypting messages: {e}")

if __name__ == "__main__":
    main()
