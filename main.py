import json
import logging
from datetime import datetime
from os import name

import pandas as pd
import requests

from settings import API_ENDPOINT, DATA_PATH, MIN_BIKES_FOR_ALERT, STATIONS_TO_FOLLOW

logger = logging.getLogger()


def get_velov_data(api_endpoint: str = API_ENDPOINT):

    try:
        http_response = requests.get(api_endpoint)
    except Exception as e:
        logger.error("Error when requesting velo'v API.")
        raise e

    json_data_str = http_response.text
    json_data_dict = json.loads(json_data_str)

    data_df = pd.DataFrame.from_dict(json_data_dict["values"])
    data_df["request_date"] = datetime.now()
    data_df["last_update"] = pd.to_datetime(data_df.last_update)

    return data_df


def remove_data_already_saved(df_hist: pd.DataFrame, new_data_df: pd.DataFrame):

    last_request_date = df_hist["request_date"].sort_values().tail(1).item()
    last_hist_data = df_hist[df_hist.request_date == last_request_date]

    joined_data = pd.merge(
        new_data_df, last_hist_data, on="number", how="left", suffixes=("", "_old")
    )

    # Join old data with new data and keep only new data lines with last update
    # earlier than old data last update.
    # Also keep new data lines that does not appear in new data
    # and thus have NaN old data last update.
    new_data_to_keep = joined_data.loc[
        (joined_data.last_update > joined_data.last_update_old)
        | joined_data.last_update_old.isna(),
        ~joined_data.columns.str.endswith("_old"),
    ]

    return new_data_to_keep


def main():

    velov_data = get_velov_data(API_ENDPOINT)

    logger.info(f"Scraped data from {velov_data.shape[0]} velo'v stations.")

    if not DATA_PATH.exists():
        logger.info("No historical data found, creating new bistorical data file.")
        velov_data.to_parquet(DATA_PATH)
    else:
        old_hist_data = pd.read_parquet(DATA_PATH)
        data_to_add = remove_data_already_saved(old_hist_data, velov_data)
        logger.info(
            f"Adding {data_to_add.shape[0]} stations that have been updated since last time."
        )
        hist_data = pd.concat((old_hist_data, data_to_add))
        hist_data.to_parquet(DATA_PATH)


if __name__ == "__main__":
    logger.info("Velo'v data scraping process launched.")
    main()
    logger.info("Velo'v data scraping process finished.")