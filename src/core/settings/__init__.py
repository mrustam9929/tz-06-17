import os

from dotenv import load_dotenv

load_dotenv()
DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE', 'LOCAL')
if DEVELOPMENT_MODE == 'DEVELOPMENT':
    from .development import *
if DEVELOPMENT_MODE == 'DEVELOPMENT':
    from .development import *
elif DEVELOPMENT_MODE == 'PRODUCTION':
    from .production import *
