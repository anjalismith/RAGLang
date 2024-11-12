FROM python:3.10-slim

WORKDIR /compiler

COPY . /compiler

CMD ["python3", "-m", "parser.parser2"]

CMD ["python3", "run.py"]
