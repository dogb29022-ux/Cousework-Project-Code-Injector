import subprocess
import os

def recursive_cleanup(directory, pattern="temp_script_"):
    """
    A recursive function that searches a directory and deletes 
    any files starting with the specified pattern.
    """
    for item in os.listdir(directory):
        path = os.path.join(directory, item)