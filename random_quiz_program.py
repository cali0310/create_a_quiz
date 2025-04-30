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

        #load and shuffling questions
        self.questions = load_questions()
        if not self.questions:
            messagebox.showerror("No Questions Found", "No questions available in 'quiz_questions.txt'")
            self.master.destroy()
            return
        
        random.shuffle(self.questions)
        self.current_index=0
        self.score=0

         #display GUI Elements
        self.question_var = tk.StringVar()
        self.selected_option = tk.StringVar()

        self.create_widgets()
        self.display_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = quiz_app(root)
    root.mainloop()