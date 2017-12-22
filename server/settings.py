import os


ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))

SERVER_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

CLIENT_DIR = os.path.normpath(os.path.join(ROOT_DIR, 'client'))

TEMPLATE_PATH = os.path.normpath(os.path.join(CLIENT_DIR, 'src/templates'))