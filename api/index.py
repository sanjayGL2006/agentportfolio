import sys
import os

# Add the project root directory to sys.path to allow importing from the root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Flask app instance from app.py at the root
from app import app
