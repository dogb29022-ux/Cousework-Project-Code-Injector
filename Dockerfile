# 1. Use an official lightweight Python image
FROM python:3.10-slim

# 2. Install system dependencies for Tkinter and X11
RUN apt-get update && apt-get install -y \
    python3-tk \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy your project files into the container
COPY . /app

# 5. Set Environment Variable to connect to the host's display
# This allows the GUI to pop up on your monitor
ENV DISPLAY=host.docker.internal:0.0

# 6. Command to run your application
CMD ["python", "main.py"]