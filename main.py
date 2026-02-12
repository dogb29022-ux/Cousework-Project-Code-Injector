#TODO: main function to be defined

import tkinter as tk
import gui_components
import execution_logic
import os

def handle_execution(input_widget, output_widget):
    """
    The bridge function that gets text from the GUI and sends it to the logic.
    """
    # 1. Get code from the UI
    user_code = input_widget.get("1.0", tk.END)
    # [TODO]
    
# Initialize the main tkinter window
def start_app():
    pass


