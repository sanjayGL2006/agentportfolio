import os
import sys
import time
import shutil
import sqlite3
import pymysql
from datetime import datetime
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

def get_db_type():
    db_url = os.environ.get("DATABASE_URL")
    db_host = os.environ.get("DB_HOST")
    db_user = os.environ.get("DB_USER")
    db_name = os.environ.get("DB_NAME")
    if db_url and db_url.startswith("mysql"):
        return "mysql"
    elif db_host and db_user and db_name:
        return "mysql"
    return "sqlite"

def backup_sqlite():
    db_path = "portfolio.db"
    if not os.path.exists(db_path):
        print(f"[BACKUP] SQLite database file '{db_path}' not found. Nothing to backup.")
        return False
        
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"portfolio_backup_{timestamp}.db")
    
    try:
        shutil.copy2(db_path, backup_path)
        print(f"[BACKUP] SQLite database backed up successfully to: {backup_path}")
        return True
    except Exception as e:
        print(f"[BACKUP] Error backing up SQLite database: {e}")
        return False

def backup_mysql():
    db_host = os.environ.get("DB_HOST", "localhost")
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASSWORD", "")
    db_name = os.environ.get("DB_NAME")
    db_port = int(os.environ.get("DB_PORT", "3306"))
    
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"mysql_backup_{timestamp}.sql")
    
    print(f"[BACKUP] Connecting to MySQL database '{db_name}' to create SQL dump...")
    try:
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
        
        # Query tables in database context
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(f"-- MySQL database backup --\n")
            f.write(f"-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} --\n\n")
            f.write("SET FOREIGN_KEY_CHECKS = 0;\n\n")
            
            for table in tables:
                # Query table creation schema
                cursor.execute(f"SHOW CREATE TABLE `{table}`")
                create_stmt = cursor.fetchone()[1]
                f.write(f"DROP TABLE IF EXISTS `{table}`;\n")
                f.write(f"{create_stmt};\n\n")
                
                # Query all data rows
                cursor.execute(f"SELECT * FROM `{table}`")
                rows = cursor.fetchall()
                if rows:
                    cursor.execute(f"DESCRIBE `{table}`")
                    cols = [col[0] for col in cursor.fetchall()]
                    cols_str = ", ".join([f"`{c}`" for c in cols])
                    
                    f.write(f"-- Dumping data for table `{table}` --\n")
                    for row in rows:
                        vals = []
                        for val in row:
                            if val is None:
                                vals.append("NULL")
                            elif isinstance(val, (int, float)):
                                vals.append(str(val))
                            else:
                                escaped_val = str(val).replace("'", "''").replace("\\", "\\\\")
                                vals.append(f"'{escaped_val}'")
                        f.write(f"INSERT INTO `{table}` ({cols_str}) VALUES ({', '.join(vals)});\n")
                    f.write("\n")
                    
            f.write("SET FOREIGN_KEY_CHECKS = 1;\n")
            
        print(f"[BACKUP] MySQL database backed up successfully to: {backup_path}")
        return True
    except Exception as e:
        print(f"[BACKUP] Error backing up MySQL database: {e}")
        return False

def run_backup():
    db_type = get_db_type()
    if db_type == "sqlite":
        return backup_sqlite()
    else:
        return backup_mysql()

def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--schedule":
        try:
            interval = int(sys.argv[2])
            print(f"[BACKUP] Starting scheduled backup mode. Backups will run every {interval} seconds...")
            while True:
                run_backup()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("[BACKUP] Scheduled backup mode stopped by user.")
        except Exception as e:
            print(f"[BACKUP] Scheduler error: {e}")
    else:
        run_backup()

if __name__ == "__main__":
    main()
