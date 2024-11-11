# RAGLang: A Programming Language for Retrieval-Augmented Generation
Developed by Anjali Smith (**as6467**) and Shreeya Patel (**sjp2236**) for COMS4115: PLT Programming Assignment 1 

## Overview
RAGLang (Retrieval-Augmented Generation Language) is a programming language that combines structured data retrieval (using SQL-like queries) with natural language to output a prompt that can be sent to large language models (LLMs) for Retrieval-Augmented Generation tasks. 

## [RAGLang Lexer](lexer/README.md)
To execute our script, run the following commands:
1. `cd lexer`
2. `python3 run.py`.

## [RAGLang Parser](parser/README.md)
To execute our script, run the following commands:
1. `cd parser`
2. `python3 run.py`.


### 1. RagLang Grammar
Program -> RQG
R -> "RETRIEVE" Colon Source
Source -> "SOURCE" Colon String
Q -> "QUERY" Colon "SELECT" A "FROM" Identifier W L
W -> "WHERE" D Semicolon | Semicolon
L -> "LIMIT" Colon Number | epsilon
A -> List | "*"
List -> Identifier | Identifier Comma List
D -> Condition ("AND | OR") D | Condition
Condition -> Identifier Operator Value
Value -> String | Number
G -> "GENERATE" Colon Prompt
Prompt -> "PROMPT" Colon String

### 2. Parsing Algorithm


### 3. Sample Input Programs
* Input:
* Lexer Output (Tokenization):
* Parser Output (AST):

### 3. Sample Input Programs

### 3. Shell Script

### 3. Video






