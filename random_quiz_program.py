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
class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("General Knowledge Quiz")
        self.master.geometry("500x500")
        self.master.resizable(False, False)

        self.bg_color = "#F5ECD5"       # Light beige
        self.text_color = "#333333"     # Dark text
        self.button_color = "#626F47"   # Soft green
        self.button_hover = "#90B8AD"
        self.radio_bg = "#F5ECD5"
        self.radio_select = "#D6CDBB"

        self.master.configure(bg=self.bg_color)
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
        self.title_label = tk.Label(
            self.master, text="General Knowledge Quiz", font=("Helvetica", 20, "bold"), fg=self.text_color,
            bg=self.bg_color
        )   
        self.title_label.pack(pady=(10, 5))
        self.score_label=tk.Label(self.master, text="Score: 0", font=("Helvetica", 12, "bold"), bg=self.bg_color)
        self.score_label.pack(pady=10)
        self.question_label = tk.Label(self.master, textvariable=self.question_var, font=("Helvetica", 14), bg=self.bg_color, wraplength=450)
        self.question_label.pack(pady=20)
        self.feedback_label = tk.Label(self.master, text="", font=("Helvetica", 12, "italic"),
                               bg=self.bg_color, fg="red", wraplength=450)
        self.feedback_label.pack(pady=(0, 10))

        self.option_buttons = {}
        for opt in ['a', 'b', 'c', 'd']:
            rb = tk.Radiobutton(self.master, text="", variable=self.selected_option, value=opt,
                                font=("Helvetica", 12), bg=self.bg_color, activeforeground=self.text_color, wraplength=450, anchor="w", justify="left")
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
        q = self.questions[self.current_index]
        self.question_var.set(f"Q{self.current_index + 1}: {q['question']}")
        self.selected_option.set("")  # Clear previous selection

        for opt in ['a', 'b', 'c', 'd']:
            self.option_buttons[opt].config(text=f"{opt.upper()}. {q['choices'][opt]}")

    def check_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please choose an answer to proceed.")
            return

        correct = self.questions[self.current_index]['correct_answer']
        correct_text = self.questions[self.current_index]['choices'][correct]

        if selected == correct:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"The correct answer is: {correct.upper()}. {correct_text}", fg="red")

        self.score_label.config(text=f"Score: {self.score}")
        self.submit_button.config(state="disabled")  

        self.master.after(1000, self.next_question)
   
    def next_question(self):
        self.current_index += 1
        self.feedback_label.config(text="")  # Clear feedback
        self.submit_button.config(state="normal")
        self.display_question()

    def end_quiz(self):
        total = len(self.questions)
        messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {total}.")
        self.master.quit()

    def exit_quiz(self):
        if messagebox.askyesno("Exit Quiz", "Are you sure you want to exit? Your progress will be lost."):
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()