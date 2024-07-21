# Use python 3.8 slim image as base image
FROM python:3.8-slim

# Set the author of the image
LABEL maintainer="Luong Cong Dan <lcd11001@gmail.com>"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the ROOT working directory
WORKDIR /app

# Copy the dependencies file to the ROOT
COPY docker_requirements.txt .

# Set the SOURCE working directory
WORKDIR /app/src

# Copy the source code to the SOURCE
COPY image_2_ascii.py .

# Grant execute permissions to all .py files
RUN chmod +x *.py

# Install any dependencies
RUN pip install --no-cache-dir -r /app/docker_requirements.txt

# Run the application
CMD ["python", "image_2_ascii.py", "--help"]

