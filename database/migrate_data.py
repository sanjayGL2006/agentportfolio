import os
import json
import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
# Import models from your app.py if needed, or we can use raw SQLAlchemy core to migrate data.
try:
    from app import app, db, Project, Certificate
except ImportError:
    print("Run this script from the root directory: python database/migrate_data.py")
    exit(1)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TODO: PASTE YOUR SUPABASE POSTGRESQL CONNECTION STRING HERE
# You can find this in your Supabase Dashboard -> Project Settings -> Database -> Connection string (URI)
# It should look like: postgresql://postgres.[project-ref]:[password]@aws-0-eu-central-1.pooler.supabase.com:6543/postgres
SUPABASE_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://...")

def migrate():
    if SUPABASE_DATABASE_URL == "postgresql://...":
        logger.error("Please set your SUPABASE_DATABASE_URL in the script or in your .env file!")
        return

    logger.info(f"Connecting to Supabase Database...")
    
    # We will override the Flask app configuration to use Supabase
    app.config['SQLALCHEMY_DATABASE_URI'] = SUPABASE_DATABASE_URL
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_pre_ping': True}
    
    with app.app_context():
        logger.info("Creating tables on Supabase...")
        db.create_all()
        
        # Now we read from the local SQLite database and insert into Supabase
        # Or, we can just let the app's built-in startup logic migrate from JS -> SQL!
        logger.info("Tables created successfully. You can now start 'python app.py'")
        logger.info("The app will automatically sync your projectsData.js and certificatesData.js into Supabase on startup!")

if __name__ == "__main__":
    migrate()
