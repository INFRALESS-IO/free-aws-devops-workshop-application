# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
# The default port for Python's HTTP server is not defined, so we'll use 8000
EXPOSE 8000

# Run app.py when the container launches
# Note: Python does not have a default port like some web servers (e.g., Apache's 80)
# So, we will run a simple HTTP server on port 8000 as an example
CMD ["python", "-m", "http.server", "8000"]
