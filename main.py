import json
import logging
from datetime import datetime
from os import name
import time

import pandas as pd
import requests

from settings import API_ENDPOINT, DATA_PATH, SLEEP_TIME
from database_handler import DatabaseHandler

logger = logging.getLogger()


def get_velov_data(api_endpoint: str = API_ENDPOINT) -> pd.DataFrame:
    """Request the velo'v API endpoint to get data from stations.

    Parameters
    ----------
    api_endpoint : str
        URL of the API endpoint. See settings.py for default value.

    Returns
    -------
    DataFrame
        DataFrame containing the velo'v data.
    """
    try:
        http_response = requests.get(api_endpoint)
    except Exception as e:
        logger.error(f"Error when requesting velo'v API :{e}")
        raise e

    json_data_str = http_response.text
    json_data_dict = json.loads(json_data_str)

    data_df = pd.DataFrame.from_dict(json_data_dict["values"])
    data_df["request_date"] = datetime.now()
    data_df["last_update"] = pd.to_datetime(data_df.last_update)

    return data_df


def main():
    db_handler = DatabaseHandler(DATA_PATH)

    while True:
        logger.info("Velo'v data scraping process launched.")

        velov_data = get_velov_data(API_ENDPOINT)

        logger.info(f"Scraped data from {velov_data.shape[0]} velo'v stations.")

        if db_handler.get_db_count() == 0:

            logger.info(
                "No historical data found, inersting new historical data to db."
            )

            db_handler.insert_data(velov_data)

        else:
            new_data_to_add_df = db_handler.filter_old_data(velov_data)

            if new_data_to_add_df.shape[0] > 0:
                logger.info(
                    f"Adding {new_data_to_add_df.shape[0]} stations that have been updated since last time."
                )
                db_handler.insert_data(new_data_to_add_df)
            else:
                logger.info("No new data")

        logger.info("Velo'v data scraping process finished.")
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    logger.info(f"Process starting with sleep time {SLEEP_TIME}")
    main()
