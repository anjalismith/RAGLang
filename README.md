# RAGLang: A Programming Language for Retrieval-Augmented Generation
Anjali Smith (as6467) and Shreeya Patel (sjp2236)
## Overview
RAGLang (Retrieval-Augmented Generation Language) is a programming language that combines structured data retrieval (using SQL-like queries) with natural language to output a prompt that can be sent to large language models (LLMs) for Retrieval-Augmented Generation tasks. 

## Lexer
Lexical Specification of RagLang: 
Keywords: "RETRIEVE" + "GENERATE" + "SELECT" + "FROM" + "WHERE" + "LIMIT" + "OR" + "AND" + "QUERY" + "PROMPT"
Identifiers: [a-zA-Z][a-zA-Z0-9_]*
Number: [0-9]+
Semicolon: ":"
Comma: ","
Operators: "==" + "<" + ">" + "<=" + ">=" + "!=" + "*"
Whitespace: [" " + "\t" + "\n"]+ (newlines, tabs, and blanks)
String: "[^"]*"

