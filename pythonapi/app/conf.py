import os
import logging
from pathlib import Path

from dotenv import load_dotenv

logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_format = '%(asctime)s | %(process)d - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)

MAIN_PATH = Path().cwd()

env_file = load_dotenv()

DOMAIN = os.getenv("DOMAIN")
WORKSPACE = os.getenv("WORKSPACE")
SERVICE_VERSION = os.getenv("SERVICE_VERSION")
LAYER_NAME = os.getenv("LAYER_NAME")
PYTHON_API_PORT = os.getenv("PYTHON_API_PORT")

# domain = "https://geoserver.massimilianomoraca.me"
# workspace = "MassimilianoMoraca"
# service_version = "1.3.0"
# layer_name = "edificicasalnuovo"
