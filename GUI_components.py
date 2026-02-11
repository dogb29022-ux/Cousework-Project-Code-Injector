import tkinter as tk
from tkinter import scrolledtext

def create_widgets(root, run_callback):
    """
    Creates the UI elements and places them in the window.
    """
    # Header Label
    header = tk.Label(root, text="Python Code Injector", font=("Arial", 16, "bold"))
    header.pack(pady=10)