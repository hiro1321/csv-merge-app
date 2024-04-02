# sqlite_processor.py

import sqlite3
import pandas as pd
import os
from source.config import settings


class DatabaseConnection:
    def __enter__(self):
        self.conn = sqlite3.connect(settings.DATABASE_PATH)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()


def initialize_database():
    if not os.path.exists(settings.DATABASE_PATH):
        with DatabaseConnection() as conn:
            conn.close()


def table_exists(table_name):
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,),
        )
        return cursor.fetchone() is not None


def execute_ddl_script():
    with open(settings.DDL_SCRIPT_PATH, "r") as file:
        ddl_script = file.read()

    if not table_exists(settings.TABLE_NAME):
        with sqlite3.connect(settings.DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.executescript(ddl_script)
            conn.commit()


def delete_all():
    query = f"DELETE FROM {settings.TABLE_NAME}"
    with DatabaseConnection() as conn:
        conn.cursor().execute(query)
        conn.commit()


def insert(df: pd.DataFrame):
    with DatabaseConnection() as conn:
        df.to_sql(settings.TABLE_NAME, conn, if_exists="append", index=False)


def select_all() -> pd.DataFrame:
    query = f"SELECT * FROM {settings.TABLE_NAME}"
    df = pd.DataFrame()
    with DatabaseConnection() as conn:
        df = pd.read_sql_query(query, conn)
    return df


initialize_database()
execute_ddl_script()
