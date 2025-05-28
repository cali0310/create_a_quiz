import tkinter as tk

class ExitButton(tk.Button):
    def __init__(self, master, command):
        super().__init__(
            master,
            text="Exit",
            font=("Helvetica", 12),
            fg="red",
            command=command
        )