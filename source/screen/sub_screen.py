import tkinter as tk
from processor import csv_processor
from objects.file_paths import FilePaths


# サブスクリーンのフォーマット
def show_sub_screen(root, before_frame: tk.Frame):
    before_frame.forget()
    sub_screen = tk.Frame(root)
    sub_screen.pack()

    input1_label = tk.Label(sub_screen, text="サブスクリーンです")
    input1_label.grid(row=0, column=0, padx=5, pady=5)
