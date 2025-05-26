import tkinter as tk

class SubmitButton(tk.Button):
    def __init__(self, master, command):
        super().__init__(
            master,
            text="Submit",
            font=("Helvetica", 12),
            command=command
        )

    def enable(self):
        self.config(state="normal")

    def disable(self):
        self.config(state="disabled")