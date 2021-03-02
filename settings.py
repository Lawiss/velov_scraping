import logging.config
import os
import sys
from pathlib import Path

import yaml

PROJECT_PATH = Path(__file__).parent.absolute()

ENV_VARS = os.environ.copy()

API_ENDPOINT = (
    "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json"
)
STATIONS_TO_FOLLOW = ["Faure / Meynis"]

# APP settings
MIN_BIKES_FOR_ALERT = 1


# Data config
DATA_PATH = PROJECT_PATH / "data/velov_hist_data.pkl.compress"

# Logging configuration
LOG_CONFIG_FILE_PATH = PROJECT_PATH / "logging_config.yml"
LOG_FILE_PATH = PROJECT_PATH / "logs/app.log"
log_config = yaml.load(open(LOG_CONFIG_FILE_PATH))
log_config["handlers"]["file"]["filename"] = LOG_FILE_PATH
logging.config.dictConfig(log_config)
