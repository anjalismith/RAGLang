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

#### Sample Input 1 - Testing SELECT syntax with list of columns, limit syntax, and a complex WHERE clause
* Input:
```RETRIEVE:
        SOURCE: "SalesDB.json"
        QUERY: SELECT product, total_sales FROM sales_data WHERE year = "2023" AND region = "North America";
        LIMIT: 5
    GENERATE:
        PROMPT: "Summarize the top-performing products in a brief report highlighting key sales figures and top products"```
* Lexer Output (Tokenization):
* Parser Output (AST):

#### Sample Input 2 - Testing complex query with the use of the * operator in the SELECT clause
* Input: 
```
RETRIEVE:
    SOURCE: "InventoryDB.json" 
    QUERY: SELECT * FROM products WHERE stock > 50 AND category = "electronics";
    LIMIT: 20 
GENERATE: 
    PROMPT: "List all products with sufficient stock and catchy slogans for each product that we can use on our company social media"
```

* Lexer Output (Tokenization)
* Parser Output (AST):

### Sample Input 3 - Testing syntax error due to missing semicolon in WHERE clause
```
RETRIEVE: 
    SOURCE: "Sales.json" 
    QUERY: SELECT product_id FROM sales_data WHERE quantity > 10
    LIMIT: 5 
GENERATE:
    PROMPT: "Summarize sales data to generate a motivational message that I can use to deliver to our salespeople for their hardwork this quarter."
```

### Sample Input 4 - Testing syntax error due to missing colon after RETRIEVE

```
RETRIEVE
    SOURCE: "Analytics.json" 
    QUERY: SELECT region FROM demographics WHERE age > 18;
    LIMIT: 10 
GENERATE: 
    PROMPT: "Provide a summary of regional demographics and turn it into an abstract for our report"
```

### Sample Input 5 - Testing syntax error due to missing QUERY keyword

```
RETRIEVE: 
    SOURCE: "CustomerDB.json" 
    SELECT customer_id, purchase_amount FROM transactions WHERE purchase_amount > 100 AND loyalty_status = "Gold";
    GENERATE: 
        PROMPT: "Summarize high-value transactions"
```


### 4. Shell Script

### 5. Video






