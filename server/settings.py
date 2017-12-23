import os


ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '../'))
SERVER_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
CLIENT_DIR = os.path.normpath(os.path.join(ROOT_DIR, 'client'))

TEMPLATE_PATH = os.path.normpath(os.path.join(CLIENT_DIR, 'src/templates'))

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB_NAME = 'chatter'
