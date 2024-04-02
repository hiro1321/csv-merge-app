import os
import sys


if sys.argv[0].endswith(".py"):
    # python実行を想定
    BASE_DIR = os.path.abspath(os.path.join(__file__, "../../../"))
else:
    # 実行ファイルを想定
    exe_path = sys.executable
    BASE_DIR = os.path.dirname(exe_path)

print(BASE_DIR)
DATABASE_NAME = "data.db"
DATABASE_PATH = os.path.join(BASE_DIR, DATABASE_NAME)
DDL_SCRIPT_PATH = os.path.join(BASE_DIR, "ddl/create_tables.sql")
TABLE_NAME = "sample_data"
OUTPUT_FILE_NAME = "output.csv"
# TODO:実データのレイアウトに修正
TABLE_COLUMNS = ["id", "column1", "column2", "column3"]
