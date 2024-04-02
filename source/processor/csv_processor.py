from tkinter import filedialog
import pandas as pd
from source.config import settings


def select_input_file():
    return filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])


def select_output_directory():
    return filedialog.askdirectory()


def read_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    if all(column in df.columns for column in settings.TABLE_COLUMNS):
        target_columns_df = df[settings.TABLE_COLUMNS].copy()
    else:
        existing_columns = [
            column for column in settings.TABLE_COLUMNS if column in df.columns
        ]
        target_columns_df = (
            df[existing_columns].copy() if existing_columns else pd.DataFrame()
        )

    # 入力データを加工する場合、ここに処理を記載

    return target_columns_df


def write_csv(file_path: str, df: pd.DataFrame):
    df.to_csv(file_path + "/" + settings.OUTPUT_FILE_NAME, index=False)
