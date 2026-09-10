import os
import sys
import dotenv
from pathlib import Path
import django

# Add the repository directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load env vars
env_path = Path(__file__).resolve().parent.parent / '.env'
dotenv.load_dotenv(env_path)

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repository.settings')
django.setup()

from library.databases.service import mongo_DB

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

print(f"Connecting with user: {MONGO_USERNAME}")

try:
    client = mongo_DB(MONGO_USERNAME, MONGO_PASSWORD)
    # Try a search that would trigger the new logic
    query = "test"
    print(f"Searching for: {query}")
    results = client.search_document(query, {})
    print(f"Found {len(results)} results")
except Exception as e:
    print(f"Caught exception: {e}")
