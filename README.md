# RAGLang: A Programming Language for Retrieval-Augmented Generation
Developed by Anjali Smith (**as6467**) and Shreeya Patel (**sjp2236**) for COMS4115: PLT Programming Assignment 1 

## Overview
RAGLang (Retrieval-Augmented Generation Language) is a programming language that combines structured data retrieval (using SQL-like queries) with natural language to output a prompt that can be sent to large language models (LLMs) for Retrieval-Augmented Generation tasks. 

## [RAGLang Lexer](lexer/README.md)
To execute our script, run the following commands:
1. `cd lexer`
2. `python3 run.py`.

## RAGLang Parser
If you have Python installed, you can execute our script by running the following command:

1. `cd parser`
2. `python3 run.py`.


Otherwise, if you don't have Python installed, we have set up a Dockerfile. Use the following instructions to build and run the Docker container:
1. Install Docker Desktop from Docker's official website.
2. In the root directory, run
```docker build -t raglang-parser .```
3. Once its built, run the container with:
```docker run --rm raglang-parser```

## RAGLang Code Generator

## Database
To open the database, run `sqlite3 sample.db` 

To see all the tables in your database, run `.tables`

To see the schema of a specific table, run `.schema <table name>`

To exit, run `.exit`

## Sample Programs

## Video