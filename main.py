#TODO: main function to be defined

import tkinter as tk
import GUI_components
import execution_logic
import os

def handle_execution(input_widget, output_widget):
    """
    The bridge function that gets text from the GUI and sends it to the logic.
    """
    code = input_widget.get("1.0", tk.END)

    report = execution_logic.inject_and_run(code)   # or whatever your function is

    output_widget.delete("1.0", tk.END)

    if report is None:
        output_widget.insert(tk.END, "No output generated.")
    else:
        output_widget.insert(tk.END, str(report))
    
    

# Initialize the main tkinter window
def start_app():
   # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("Python Injector Tool")
    root.geometry("500x550")

    # Build the GUI
    GUI_components.create_widgets(root, handle_execution)

    # Start the event loop
    root.mainloop()

if __name__=="__main__":
    start_app()


