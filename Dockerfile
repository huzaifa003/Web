# Use the official Python image as a base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
