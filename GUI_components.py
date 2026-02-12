import tkinter as tk
from tkinter import scrolledtext

def create_widgets(root, run_callback):
    """
    Creates the UI elements and places them in the window.
    """
    # Header Label
    header = tk.Label(root, text="Python Code Injector", font=("Arial", 16, "bold"))
    header.pack(pady=10)

    # Input Area (Where you type code)
    tk.Label(root, text="Enter Python Code:").pack()
    input_area = scrolledtext.ScrolledText(root, height=10, width=50)
    input_area.pack(pady=5)
    