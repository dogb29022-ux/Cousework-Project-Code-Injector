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
    
    # 2. Clean up old temp files recursively before running
    execution_logic.recursive_cleanup(os.getcwd())
    
    # 3. Run the code and get the result
    report = execution_logic.inject_and_run(user_code)
    
    # 4. Update the UI with the result
    output_widget.delete("1.0", tk.END)
    output_widget.insert(tk.END, report)

# Initialize the main tkinter window
def start_app():
   # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("Python Injector Tool")
    root.geometry("500x550")

    # Build the GUI
    gui_components.create_widgets(root, handle_execution)

    # Start the event loop
    root.mainloop()

if __name__=="__main__":
    start_app()


