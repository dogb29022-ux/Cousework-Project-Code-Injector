import subprocess
import os

def recursive_cleanup(directory, pattern="temp_script_"):
    """
    A recursive function that searches a directory and deletes 
    any files starting with the specified pattern.
    """
    for item in os.listdir(directory):
        path = os.path.join(directory, item)

        # If it's a directory, recurse into it
        if os.path.isdir(path):
            recursive_cleanup(path, pattern)
        # If it's a file and matches our temp pattern, delete it
        elif item.startswith(pattern) and item.endswith(".py"):
            os.remove(path)