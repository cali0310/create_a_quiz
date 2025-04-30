import tkinter as tk
from tkinter import messagebox
import json
import random
import os

# Create the main window
root = tk.Tk()
root.title("GUI TESTING")
root.geometry("300x200")  # Width x Height

# Add a label
label = tk.Label(root, text="CODE TEST FOR GUI!")
label.pack(pady=20)

# Add a button
button = tk.Button(root, text="TESTING", command=lambda: label.config(text="You clicked the button. Press X to exit"))
button.pack()

# Run the GUI loop
root.mainloop()