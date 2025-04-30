import tkinter as tk
from tkinter import messagebox
import json
import random
import os

# creating main window
root = tk.Tk()
root.title("GUI TESTING")
root.geometry("300x200")  # Width x Height

# label
label = tk.Label(root, text="CODE TEST FOR GUI!")
label.pack(pady=20)

# button
button = tk.Button(root, text="TESTING", command=lambda: label.config(text="You clicked the button. Press X to exit"))
button.pack()

# run GUI loop
root.mainloop()