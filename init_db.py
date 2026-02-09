
import os
import sys
import logging
from pathlib import Path

# Add repo root to python path
repo_root = Path(__file__).resolve().parent
sys.path.insert(0, str(repo_root))

from PySide6.QtCore import QCoreApplication
from openlp.core.common.applocation import AppLocation
from openlp.core.common.settings import Settings
from openlp.core.db.manager import DBManager

# Mocking QApp somewhat or just setting up logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def main():
    # Initialize QCoreApplication for Settings and other Qt-dependent parts
    app = QCoreApplication(sys.argv)
    app.setApplicationName('OpenLP')
    app.setOrganizationName('OpenLP')
    
    # Initialize Registry
    from openlp.core.common.registry import Registry
    Registry.create()
    
    # 2. Trigger Settings (will load .env due to our previous change)
    settings = Settings()
    Registry().register('settings', settings)
    print("Settings loaded and registered.")

    print("Initializing OpenLP Configuration and Database...")
    
    # 1. Setup AppConfig
    # We need to make sure AppLocation is happy.
    # AppLocation.get_directory usually determines paths based on OS.
    # We might need to mock or ensure the "portable" logic if we want to force location, 
    # but for now let's rely on default detection.
    
    # Check if we are portable (optional, based on env var maybe?)
    # For now, standard initialization.
    
    data_path = AppLocation.get_data_path()
    print(f"Data Path: {data_path}")
    
    # AppLocation.get_directory usually determines paths based on OS.
    # OpenLP core doesn't have a massive single DB, it has plugins.
    # However, 'songs', 'bibles', etc are plugins. 
    # Let's initialize the 'songs' DB as a proof of concept/essential step.
    # But wait, DBManager is usually instantiated per plugin.
    
    # Let's verify if there is a 'core' db.
    # Looking at openlp/core/db/manager.py, it takes a plugin name.
    
    # Let's iterate typical plugins and init them if possible, or just the main one.
    # Many plugins are in openlp/plugins.
    
    # For this task, "ensure database is setup", we'll init the 'songs' database 
    # which is the most critical user data usually.
    
    from openlp.plugins.songs.lib import db as song_db
    from openlp.plugins.songs.lib import upgrade as song_upgrade
    
    print("Initializing 'songs' database...")
    db_manager = DBManager('songs', song_db.init_schema, upgrade_mod=song_upgrade)
    
    if db_manager and db_manager.session:
        print("Songs database initialized successfully.")
    else:
        print("Failed to initialize songs database.")
        sys.exit(1)
        
    print("Database setup complete.")

if __name__ == "__main__":
    main()
