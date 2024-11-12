# Use a Python 3 image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /compiler

# Copy the entire project into the container
COPY . /compiler

CMD ["python3", "-m", "parser.parser2"]