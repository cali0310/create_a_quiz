import tkinter as tk

class FeedbackDisplay(tk.Label):
    def __init__(self, master):
        super().__init__(
            master,
            text="",
            font=("Helvetica", 12, "italic"),
            bg="#F5ECD5",
            fg="red",
            wraplength=450
        )

    def show_feedback(self, message, color):
        self.config(text=message, fg=color)

    def clear(self):
        self.config(text="")