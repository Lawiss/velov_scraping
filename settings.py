import os
from pathlib import Path

ENV_VARS = os.environ.copy()

API_ENDPOINT = (
    "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json"
)
STATIONS_TO_FOLLOW = ["Faure / Meynis"]

# APP settings
MIN_BIKES_FOR_ALERT = 1

PROJECT_PATH = Path(__file__).parent.absolute()
DATA_PATH = PROJECT_PATH / "data/velov_hist_data.parquet"
