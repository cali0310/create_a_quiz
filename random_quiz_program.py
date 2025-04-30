import tkinter as tk
from tkinter import messagebox
import json
import random
import os

def load_questions(file_name="quiz_questions.txt"):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

# GUI for quiz
class quiz_app:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz")
        self.master.geometry("500x450")
        self.master.resizable(False, False)

if __name__ == "__main__":
    root = tk.Tk()
    app = quiz_app(root)
    root.mainloop()