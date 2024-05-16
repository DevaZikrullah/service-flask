# Use the official Python image as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container at /app
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5001

# Run the Flask app
CMD ["python", "main.py"]
