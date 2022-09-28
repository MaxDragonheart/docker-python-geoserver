import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_format = '%(asctime)s | %(process)d - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)


domain = "https://geoserver.massimilianomoraca.me"
workspace = "MassimilianoMoraca"
service_version = "1.3.0"
layer_name = "edificicasalnuovo"
layer_type = "vector"