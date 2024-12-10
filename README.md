# RAGLang: A Programming Language for Retrieval-Augmented Generation
Developed by Anjali Smith (**as6467**) and Shreeya Patel (**sjp2236**) for COMS4115: PLT Programming Assignment 3

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

If you have Python installed, you can execute our script by running the following command:

`python3 run.py`

## Database
### Installation:

SQLite is typically pre-installed on many systems, but you can check by running:
`sqlite3 --version`

If it's not installed, you can install it:

**Ubuntu/Debian**:
`sudo apt-get install sqlite3`

**MacOS (via Homebrew)**:
`brew install sqlite`

**Windows**: 
Download SQLite from the [official website](https://www.sqlite.org/download.html) and follow the installation instructions.

### Commands
To open the database, run `sqlite3 <name of database>` ie, `sqlite3 sales-2024.db`

To see all the tables in your database, run `.tables`

To see the schema of a specific table, run `.schema <table name>`

To exit, run `.exit`

## Sample Programs

#### Sample Input 1 - Testing the code generation phase on the customers table
* Input:
```
    RETRIEVE: 
        SOURCE: "sales-2024.db" 
        QUERY: SELECT name, email FROM customers WHERE active = "true";
        LIMIT: 10
    GENERATE:
        PROMPT: "Create a different thank you message for each customer."
```


* Parser Output (AST):
```
                        'Program'
        'R'
                'Keyword': 'RETRIEVE'
                'Source'
                        'Keyword': 'SOURCE'
                        'String': 'sales-2024.db'
        'Q'
                'Keyword': 'QUERY'
                'Keyword': 'SELECT'
                'A'
                        'List'
                                'Identifier': 'name'
                                'Identifier': 'email'
                'Keyword': 'FROM'
                'Identifier': 'customers'
                'Where'
                        'Keyword': 'WHERE'
                        'Condition'
                                'Identifier': 'active'
                                'Operator': '='
                                'Value': 'true'
                'L'
                        'Keyword': 'LIMIT'
                        'Number': '10'
        'G'
                'Keyword': 'GENERATE'
                'Prompt'
                        'Keyword': 'PROMPT'
                        'String': 'Create a different thank you message for each customer.'

```
* RagLang Output:
```
====================================================================================================
🌟 RAGLANG OUTPUT 🌟
Copy and paste the following text into the AI assistant of your choice (e.g., ChatGPT, Claude)
====================================================================================================

Please respond to the following prompt using the provided data.

Data:
- John Doe, john.doe@example.com
- Jane Smith, jane.smith@example.com
- Michael Brown, michael.brown@example.com
- Emma Wilson, emma.wilson@example.com
- Aaron Lilac, a.lilac@example.com
- Mike Roger, mike.r@example.com
- Izzy Tike, izzy.tike@example.com

Prompt: Create a different thank you message for each customer.
```
#### Sample Input 2 - Testing the code generation phase for complex query on the sales_data table
* Input: 
```
    RETRIEVE: 
        SOURCE: "sales-2024.db" 
        QUERY: SELECT product, total_sales FROM sales_data 
        WHERE year = 2023 AND total_sales > 4000 AND region = "North America";
    GENERATE: 
        PROMPT: "Write catchy descriptions of each of our top-selling products in 2023 for North America that we can use on our social media page."
```

* Parser Output (AST):
```
AST:  'Program'
        'R'
                'Keyword': 'RETRIEVE'
                'Source'
                        'Keyword': 'SOURCE'
                        'String': 'sales-2024.db'
        'Q'
                'Keyword': 'QUERY'
                'Keyword': 'SELECT'
                'A'
                        'List'
                                'Identifier': 'product'
                                'Identifier': 'total_sales'
                'Keyword': 'FROM'
                'Identifier': 'sales_data'
                'Where'
                        'Keyword': 'WHERE'
                        'D'
                                'D'
                                        'Condition'
                                                'Identifier': 'year'
                                                'Operator': '='
                                                'Value': '2023'
                                        'Keyword': 'AND'
                                        'Condition'
                                                'Identifier': 'total_sales'
                                                'Operator': '>'
                                                'Value': '4000'
                                'Keyword': 'AND'
                                'Condition'
                                        'Identifier': 'region'
                                        'Operator': '='
                                        'Value': 'North America'
        'G'
                'Keyword': 'GENERATE'
                'Prompt'
                        'Keyword': 'PROMPT'
                        'String': 'Write catchy descriptions of each of our top-selling products in 2023 for North America that we can use on our social media page.'
```
* RagLang Output:
```
====================================================================================================
🌟 RAGLANG OUTPUT 🌟
Copy and paste the following text into the AI assistant of your choice (e.g., ChatGPT, Claude)
====================================================================================================

Please respond to the following prompt using the provided data.

Data:
- Barbie Doll, 5000
- Coffee Mug, 4500
- Sneakers, 6000
- Headphones, 5000
- Suitcase, 4500
- Soap, 6000

Prompt: Write catchy descriptions of each of our top-selling products in 2023 for North America that we can use on our social media page.
```

### Sample Input 3 - Testing the code generation phase on the inventory table
```
    RETRIEVE:
        SOURCE: "sales-2024.db"
        QUERY: SELECT product_name FROM inventory WHERE stock < 25;
        LIMIT: 5
    GENERATE:
        PROMPT: "Create a 2-month marketing campaign to advertise our lowest selling products, which will be 25% off during Black Friday"
```

Parser Output:
```
'Program'
        'R'
                'Keyword': 'RETRIEVE'
                'Source'
                        'Keyword': 'SOURCE'
                        'String': 'sales-2024.db'
        'Q'
                'Keyword': 'QUERY'
                'Keyword': 'SELECT'
                'A'
                        'List'
                                'Identifier': 'product_name'
                'Keyword': 'FROM'
                'Identifier': 'inventory'
                'Where'
                        'Keyword': 'WHERE'
                        'Condition'
                                'Identifier': 'stock'
                                'Operator': '<'
                                'Value': '25'
                'L'
                        'Keyword': 'LIMIT'
                        'Number': '5'
        'G'
                'Keyword': 'GENERATE'
                'Prompt'
                        'Keyword': 'PROMPT'
                        'String': 'Create a 2-month marketing campaign to advertise our lowest selling products, which will be 25% off during Black Friday'
```
* RagLang Output
```
====================================================================================================
🌟 RAGLANG OUTPUT 🌟
Copy and paste the following text into the AI assistant of your choice (e.g., ChatGPT, Claude)
====================================================================================================

Please respond to the following prompt using the provided data.

Data:
- Vitamins
- Lamp
- Charger

Prompt: Create a 2-month marketing campaign to advertise our lowest selling products, which will be 25% off during Black Friday
```
### Sample Input 4 - Testing semantic error due to "no such column" SQL error
* Input
```
    RETRIEVE:
        SOURCE: "sales-2024.db"\nQUERY: SELECT product_id FROM sales_data WHERE quantity > 10;LIMIT: 5
    GENERATE:
        PROMPT: "Summarize sales data to generate a motivational message that I can use to deliver to our salespeople for their hardwork this quarter."
```

* Parser Output: 
```
'Program'
        'R'
                'Keyword': 'RETRIEVE'
                'Source'
                        'Keyword': 'SOURCE'
                        'String': 'sales-2024.db'
        'Q'
                'Keyword': 'QUERY'
                'Keyword': 'SELECT'
                'A'
                        'List'
                                'Identifier': 'product_id'
                'Keyword': 'FROM'
                'Identifier': 'sales_data'
                'Where'
                        'Keyword': 'WHERE'
                        'Condition'
                                'Identifier': 'quantity'
                                'Operator': '>'
                                'Value': '10'
                'L'
                        'Keyword': 'LIMIT'
                        'Number': '5'
        'G'
                'Keyword': 'GENERATE'
                'Prompt'
                        'Keyword': 'PROMPT'
                        'String': 'Summarize sales data to generate a motivational message that I can use to deliver to our salespeople for their hardwork this quarter.'
```

### Sample Input 5 - Testing syntax error due to missing QUERY keyword
* Input
```
    RETRIEVE:
        SOURCE: "sales-2024.db"
        SELECT customer_id, purchase_amount FROM transactions WHERE purchase_amount > 100 AND loyalty_status = "Gold";
    GENERATE:
        PROMPT: "Summarize high-value transactions"
```
* Output:
```
Syntax error: Expected KEYWORD 'QUERY' at position 5
AST: None
```


## Video