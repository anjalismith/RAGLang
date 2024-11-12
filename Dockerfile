# Use a Python 3 image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the container
COPY . /app

# Change directory to the parser folder and run parser2.py
CMD ["python", "parser/parser2.py"]
