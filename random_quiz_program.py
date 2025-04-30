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

    def create_widgets(self):
        self.score_label=tk.Label(self.master, text="Score: 0", font=("Helvetica", 12, "bold"))
        self.score_label.pack(pady=10)
        self.question_label = tk.Label(self.master, textvariable=self.question_var, font=("Helvetica", 14), wraplength=450)
        self.question_label.pack(pady=20)

        self.option_buttons = {}
        for opt in ['a', 'b', 'c', 'd']:
            rb = tk.Radiobutton(self.master, text="", variable=self.selected_option, value=opt,
                                font=("Helvetica", 12), wraplength=450, anchor="w", justify="left")
            rb.pack(anchor="w", padx=40, pady=2)
            self.option_buttons[opt] = rb

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, font=("Helvetica", 12))
        self.submit_button.pack(pady=10)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.exit_quiz, font=("Helvetica", 12), fg="red")
        self.exit_button.pack(pady=5)

    def display_question(self):
        if self.current_index >= len(self.questions):
            self.end_quiz()
            return
        

if __name__ == "__main__":
    root = tk.Tk()
    app = quiz_app(root)
    root.mainloop()