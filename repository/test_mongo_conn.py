import os
from pymongo import MongoClient
from urllib.parse import quote_plus

# Simple .env parser (no external deps)
env_path = os.path.join(os.path.dirname(__file__), '.env')
conn = None
with open(env_path, 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' in line:
            k, v = line.split('=', 1)
            if k.strip() == 'DATABASE_STRING':
                conn = v.strip()
                break

print('Using connection string (trimmed):', (conn[:120] + '...') if conn else None)
try:
    client = MongoClient(conn, serverSelectionTimeoutMS=10000)
    print('Server info keys:', list(client.server_info().keys()))
    print('Databases:', client.list_database_names())
except Exception as e:
    import traceback
    traceback.print_exc()
    print('\nError type:', type(e))
    print('Error args:', e.args)
