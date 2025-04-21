# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port your app will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
