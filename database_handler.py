from pathlib import Path
import sqlite3
from typing import Union
import sqlite3

import pandas as pd
from datetime import datetime

from settings import COLUMN_NAMES


class DatabaseHandler:
    def __init__(self, database_path: Union[Path, str]) -> None:

        self.database = sqlite3.connect(database_path)
        self.init_table()

    def init_table(self) -> None:

        cur = self.database.cursor()

        cur.execute(f"CREATE TABLE IF NOT EXISTS velov {tuple(COLUMN_NAMES)}")
        self.database.commit()

    def insert_data(self, new_data_df: pd.DataFrame):
        new_data_df[COLUMN_NAMES].to_sql(
            "velov", self.database, if_exists="append", index=False
        )

    def filter_old_data(self, new_data_df: pd.DataFrame) -> pd.DataFrame:

        last_hist_data_df = self.get_last_db_data()
        joined_data = pd.merge(
            new_data_df,
            last_hist_data_df,
            on="number",
            how="left",
            suffixes=("", "_old"),
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

    def get_last_db_data(self) -> pd.DataFrame:

        last_data_df = pd.read_sql(
            "SELECT * FROM velov WHERE request_date = (SELECT request_date FROM velov ORDER BY request_date DESC LIMIT 1)",
            self.database,
        )

        return last_data_df[COLUMN_NAMES]

    def get_last_request_date(self) -> datetime:
        cursor = self.database.cursor()
        cursor.execute(
            "SELECT request_date FROM velov ORDER BY request_date DESC LIMIT 1"
        )

        res = cursor.fetchone()[0]

        last_date = datetime.strptime(res)
        return last_date

    def get_db_count(self) -> int:
        cursor = self.database.cursor()
        cursor.execute("SELECT COUNT(*) FROM velov")

        res = cursor.fetchone()[0]

        return res
