import tkinter as tk
from tkinter import filedialog
from source.screen import top_screen


def main():
    root = tk.Tk()
    root.title("CSV処理プログラム")
    root.geometry("800x400")

    top_screen.show_top_screen(root)

    root.mainloop()


if __name__ == "__main__":
    main()
