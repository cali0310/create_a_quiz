import tkinter as tk

class ScoreDisplay(tk.Label):
    def __init__(self, master):
        super().__init__(
            master,
            text="Score: 0",
            font=("Helvetica", 12, "bold"),
            bg="#F5ECD5"
        )

    def update_score(self, score):
        self.config(text=f"Score: {score}")