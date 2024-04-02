## 実行コマンド

### python 実行

```
python -m source.main

```

### exe ファイル出力

```
pyinstaller --onefile --add-data "ddl/create_tables.sql:ddl" source/main.py

```
