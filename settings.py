import logging.config
import os
import sys
from pathlib import Path

import yaml

PROJECT_PATH = Path(__file__).parent.absolute()

ENV_VARS = os.environ.copy()


# APP settings
API_ENDPOINT = (
    "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json"
)
## Default time between each process iteration call is 2.5sec
DEFAULT_SLEEP_TIME = 60
SLEEP_TIME = ENV_VARS.get("SLEEP_TIME", DEFAULT_SLEEP_TIME)


# Data config
DATA_PATH = PROJECT_PATH / "data/velov.db"
COLUMN_NAMES = [
    "number",
    "pole",
    "available_bikes",
    "code_insee",
    "lng",
    "availability",
    "availabilitycode",
    "etat",
    "startdate",
    "langue",
    "bike_stands",
    "last_update",
    "available_bike_stands",
    "gid",
    "titre",
    "status",
    "commune",
    "description",
    "nature",
    "bonus",
    "address2",
    "address",
    "lat",
    "last_update_fme",
    "enddate",
    "name",
    "banking",
    "nmarrond",
    "request_date",
]

# Logging configuration
LOG_CONFIG_FILE_PATH = PROJECT_PATH / "logging_config.yml"
LOG_FILE_PATH = PROJECT_PATH / "logs/app.log"
log_config = yaml.load(open(LOG_CONFIG_FILE_PATH))
log_config["handlers"]["file"]["filename"] = LOG_FILE_PATH
logging.config.dictConfig(log_config)
