import tkinter as tk
from source.processor import csv_processor, sqlite_processor
from source.objects.file_paths import FilePaths
from source.config import settings


def show_top_screen(root):
    top_screen = tk.Frame(root)
    top_screen.pack()

    input1_label = tk.Label(top_screen, text="入力元のCSVファイル1つめ：")
    input1_label.grid(row=0, column=0, padx=5, pady=5)

    input1_entry = tk.Entry(top_screen, width=30)
    input1_entry.grid(row=0, column=1, padx=5, pady=5)

    input1_button = tk.Button(
        top_screen,
        text="ファイルを選択",
        command=lambda: _select_input_file(input1_entry, is_first=True),
    )
    input1_button.grid(row=0, column=2, padx=5, pady=5)

    input2_label = tk.Label(top_screen, text="入力元のCSVファイル2つめ：")
    input2_label.grid(row=1, column=0, padx=5, pady=5)

    input2_entry = tk.Entry(top_screen, width=30)
    input2_entry.grid(row=1, column=1, padx=5, pady=5)

    input2_button = tk.Button(
        top_screen,
        text="ファイルを選択",
        command=lambda: _select_input_file(input2_entry, is_first=False),
    )
    input2_button.grid(row=1, column=2, padx=5, pady=5)

    output_label = tk.Label(top_screen, text="出力先ディレクトリ：")
    output_label.grid(row=2, column=0, padx=5, pady=5)
    output_entry = tk.Entry(top_screen, width=30)
    output_entry.grid(row=2, column=1, padx=5, pady=5)
    output_button = tk.Button(
        top_screen,
        text="ディレクトリを選択",
        command=lambda: _select_output_directory(output_entry),
    )
    output_button.grid(row=2, column=2, padx=5, pady=5)

    message_label = tk.Label(top_screen, text="")
    message_label.grid(row=3, column=1, padx=5, pady=5)

    execute_button = tk.Button(
        top_screen,
        text="処理を開始",
        command=lambda: _execute_job(
            message_label, input1_entry.get(), input2_entry.get(), output_entry.get()
        ),
    )
    execute_button.grid(row=4, column=1, padx=5, pady=20)


def _select_input_file(target_entry: tk.Entry, is_first: bool):
    input_file_path = csv_processor.select_input_file()
    _rewrite_entry(target_entry, input_file_path)


def _select_output_directory(target_entry: tk.Entry):
    output_directory_path = csv_processor.select_output_directory()
    _rewrite_entry(target_entry, output_directory_path)


def _rewrite_entry(entry: tk.Entry, value: str):
    entry.delete(0, tk.END)
    entry.insert(0, value)


def _execute_job(
    message_label: tk.Label,
    input_file1_path: str,
    input_file2_path: str,
    output_directory: str,
):
    file_paths = FilePaths(input_file1_path, input_file2_path, output_directory)
    if not file_paths.validate():
        message_label.configure(text="入力ファイル・出力先を選択してください")
        return

    try:
        input_df1 = csv_processor.read_csv(file_paths.input_file1_path)
        input_df2 = csv_processor.read_csv(file_paths.input_file2_path)
    except Exception as e:
        message_label.configure(text="入力ファイルが不正です")
        return

    sqlite_processor.delete_all()
    sqlite_processor.insert(input_df1)
    sqlite_processor.insert(input_df2)

    output_df = sqlite_processor.select_all()
    if len(output_df) == 0:
        message_label.configure(text="出力対象データは0件です")
        return

    csv_processor.write_csv(file_paths.output_directory, output_df)
    message_label.configure(text=f"{settings.OUTPUT_FILE_NAME}を出力しました")
