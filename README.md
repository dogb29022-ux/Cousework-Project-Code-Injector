# Project Code Injector
Python based code injector tool which can inject payload inside any files.

## Overview
This project is focused on how code injection works at conceptual and practical level. The main aim is educational purpose to explore how injectors operate,the reason to call them a security risk and how this techiniques are in  controlled enviroment like research, testing, and in learning scenarios.

overall this project replicates a hands-on learning exprience in low-level security concepts and demonstrates how theory connects with real-worls system behavior.

## Project Feature
- Utilizes the subprocess module to spawn independent child processes for script execution, preventing user-injected code from crashing or compromising the main application thread.
- Implements an automated "Write-Execute-Purge" workflow that generates unique temporary script files and ensures their immediate deletion post-execution for a zero-footprint operation.
- Captures and redirects stdout and stderr through OS pipes, allowing the GUI to display standard output and complex Python tracebacks in a unified, readable interface.
- Engineered with a strict separation of concerns, decoupling the Tkinter-based user interface from the backend execution and cleanup modules for high maintainability.
- Includes a Docker configuration using a debian-slim base image to provide a consistent, platform-independent, and secure sandboxed environment for code testing.

## Learning objective
- Developed a procedural architecture that separates GUI components from execution logic to improve code readability and maintenance.
- Implemented real-time I/O operations to transform GUI text input into executable temporary Python scripts.
- Integrated the subprocess module to run injected code in a child process, protecting the main application from crashes.
- Engineered an automated lifecycle system that purges all temporary files after execution to maintain a zero-footprint environment
- Configured a Docker environment to ensure the tool remains portable and secure within an isolated Debian-slim container

## Project Structure
```
.
├── LICENSE
├── README.md                # This file
├── execution_logic.py       # Execution logic
├── main.py                  # main file to exucute the program
├── GUI_components/oy        # GUI tkinter
├── images                   # Contains images used in documentation
    └── 
```

## Quick Start
```bash
# Clone the repository
git clone https://github.com/dogb29022-ux/Cousework-Project-Code-Injector.git
cd Coursework-Project-Code-Injector

## Install the required libraries and module
pip install requirements.txt

## Run the main application
python3 main.py
```
## Project Demonstration
**Homepage Tool**

<img src='/images/homepage-application.png' width=300 height=300>

**Code Injector In Actio**

<img src='/images/code-injector-feature.png' width=300 height=300>

## License
This project is license under MIT License. See more about [License](/LICENSE) here.

## Author
- **Shreejan Byanju** - Intial Demonstration and Work

