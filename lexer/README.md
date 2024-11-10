### 1: Lexical Specification of RagLang
Keywords: `"RETRIEVE"` + `"GENERATE"` + `"SELECT"` + `"FROM"` + `"WHERE"` + `"LIMIT"` + `"OR"` + `"AND"` + `"QUERY"` + `"PROMPT"` + `"SOURCE"`

Identifiers: `[a-zA-Z][a-zA-Z0-9_]*`

Number: `[0-9]+`

Semicolon: `":"`

Comma: `","`

Operators: `"="` + `"<"` + `">"` + `"<="` + `">="` + `"!="` + `"*"`

Whitespace: `[" " + "\t" + "\n"]+` (newlines, tabs, and blanks)

String: `"[^"]*"`

### 2: RagLang Scanning Algorithm
We defined a Lexer class in Python, which is designed to tokenize an input program. This lexer processes the input program character by character and recognizes different types of tokens, while handling transitions between various states such as "START" and "NUMBER". 

`__init__(self, input_program) Constructor`:
* Initializes the lexer with the input program which is a string containing the source code to be tokenized.
* The argument is stored in `self.input_program` allowing the lexer to process the input during scanning.

`scan(self) Method`:
* Processes the input and performs tokenization
* Represents a finite state machine, transitioning between different states based on the current character being read and the lexer’s current state.
* Returns a list of tokens in format `(<Token Type>, <Token Value>)`

#### States
1. `START` STATE

This is the default state where the lexer decides how to categorize the character based on its type.

* Alphabetic characters (char.isalpha()) -> Transition to the "IDENTIFIER" state -> collect characters to form an identifier or keyword.
* Numeric characters (char.isdigit()) -> Transition to the "NUMBER" state -> collect numeric digits to form a number.
* Special characters (;, :, ,) -> Punctuation, such as semicolon, colon, and comma and token (e.g., ("SEMICOLON", ";")) is directly added to the token list.
* Operators (=, >, <, *, !) -> Transition to the "OPERATOR" state
* String delimiters (") -> Transition to the "STRING" state to begin capturing a string literal.
* Whitespace characters ( , \t, \n) -> Ignored, the lexer continues scanning.
* Unrecognized characters -> Reports a lexical error and terminates the scanning process.

2. `IDENTIFIER` STATE
* An identifier can include letters, digits, or underscores.
* Once a non-identifier character is encountered, the lexer checks whether the accumulated curr_token is a keyword (e.g., RETRIEVE, SELECT, FROM, etc.). If it is, it adds a ("KEYWORD", curr_token) token to the list; otherwise, it adds an ("IDENTIFIER", curr_token) token.
* The lexer then transitions back to the "START" state to continue scanning.

3. `NUMBER` STATE
* The lexer collects characters as long as they are digits.
* When a non-digit character is encountered, the lexer adds a ("NUMBER", curr_token) token to the list and transitions back to the "START" state.

4. `OPERATOR` STATE
* If the current operator is a standalone operator like =, <, >, or *, the lexer adds a ("OPERATOR", curr_token) token.
* If the current operator is a multi charactered operator like !=, <= or >=, the lexer checks if the character after < or > or ! are equal signs. 
* If the operator is unrecognized, the lexer reports a lexical error.

5. `STRING` STATE
* Any character except a double quote is added to the curr_token.
* When the lexer encounters a closing double quote, it adds a ("STRING", curr_token) token to the list and transitions back to the "START" state.
* If the end of the input is reached without finding a closing quote, a lexical error is printed.

#### Error Handling
The lexer performs basic error checking while tokenizing the input:

* If a character is not part of the recognized token set, it prints out a lexical error with its position in the input.
* If the input contains an unclosed string literal, the lexer reports a lexical error.

Upon error, an empty array is returned alongside the error message which includes the unidetified token and its position in the input. 

### 3. Sample RagLang Programs and Corresponding Tokenizations
Sample programs are defined in the list `sample_programs` in the script.

#### Sample Program 1:
* Input Program: 
```RETRIEVE:\nSOURCE: "SalesDB.json"\nQUERY: SELECT product, total_sales FROM sales_data WHERE year = "2023" AND region = "North America";\nLIMIT: 5\nGENERATE:\nPROMPT: "Summarize the top-performing products in a brief report highlighting key sales figures and top products"\n```

* Expected Result: ```Tokens: [('KEYWORD', 'RETRIEVE'), ('COLON', ':'), ('KEYWORD', 'SOURCE'), ('COLON', ':'), ('STRING', 'SalesDB.json'), ('KEYWORD', 'QUERY'), ('COLON', ':'), ('KEYWORD', 'SELECT'), ('IDENTIFIER', 'product'), ('COMMA', ','), ('IDENTIFIER', 'total_sales'), ('KEYWORD', 'FROM'), ('IDENTIFIER', 'sales_data'), ('KEYWORD', 'WHERE'), ('IDENTIFIER', 'year'), ('OPERATOR', '='), ('STRING', '2023'), ('KEYWORD', 'AND'), ('IDENTIFIER', 'region'), ('OPERATOR', '='), ('STRING', 'North America'), ('SEMICOLON', ';'), ('KEYWORD', 'LIMIT'), ('COLON', ':'), ('NUMBER', '5'), ('KEYWORD', 'GENERATE'), ('COLON', ':'), ('KEYWORD', 'PROMPT'), ('COLON', ':'), ('STRING', 'Summarize the top-performing products in a brief report highlighting key sales figures and top products')]```

* Output: ```Tokens: [('KEYWORD', 'RETRIEVE'), ('COLON', ':'), ('KEYWORD', 'SOURCE'), ('COLON', ':'), ('STRING', 'SalesDB.json'), ('KEYWORD', 'QUERY'), ('COLON', ':'), ('KEYWORD', 'SELECT'), ('IDENTIFIER', 'product'), ('COMMA', ','), ('IDENTIFIER', 'total_sales'), ('KEYWORD', 'FROM'), ('IDENTIFIER', 'sales_data'), ('KEYWORD', 'WHERE'), ('IDENTIFIER', 'year'), ('OPERATOR', '='), ('STRING', '2023'), ('KEYWORD', 'AND'), ('IDENTIFIER', 'region'), ('OPERATOR', '='), ('STRING', 'North America'), ('SEMICOLON', ';'), ('KEYWORD', 'LIMIT'), ('COLON', ':'), ('NUMBER', '5'), ('KEYWORD', 'GENERATE'), ('COLON', ':'), ('KEYWORD', 'PROMPT'), ('COLON', ':'), ('STRING', 'Summarize the top-performing products in a brief report highlighting key sales figures and top products')]```

* Program Description: This program consists of every possible token in our Keyword class, operator tokens, string tokens for the database name and natural language prompt, identifier tokens, as well as colon, comma, and semicolon tokens.

#### Sample Program 2:
* Input Program:     ```RETRIEVE:\nSOURCE: "InventoryDB.csv"\nQUERY: SELECT product_name, stock FROM inventory WHERE stock < 50;\nLIMIT: 20\nGENERATE:\nPROMPT: "Create a social media caption advertising these products which have low stock levels.```

* Expected Result: 
```Lexical error: unterminated string literal 'Create a social media caption advertising these products which have low stock levels.' Tokens: []```

* Output: ```Lexical error: unterminated string literal 'Create a social media caption advertising these products which have low stock levels.' Tokens: []```

* Program Description: This program demonstrates our lexer's error handling for when an input program contains an unterminated string literal.


#### Sample Program 3:
* Input Program:  ```RETRIEVE:\nSOURCE: "FinanceData.csv"\nQUERY: SELECT * FROM accounts WHERE balance >= 10000 AND currency = "USD" AND region = "Europe";\nLIMIT: 15\nGENERATE:\nPROMPT: "Create summaries of each of the provided high-value accounts in Europe to use in a presentation."```

* Expected Result: ```Tokens: [('KEYWORD', 'RETRIEVE'), ('COLON', ':'), ('KEYWORD', 'SOURCE'), ('COLON', ':'), ('STRING', 'FinanceData.csv'), ('KEYWORD', 'QUERY'), ('COLON', ':'), ('KEYWORD', 'SELECT'), ('OPERATOR', '*'), ('KEYWORD', 'FROM'), ('IDENTIFIER', 'accounts'), ('KEYWORD', 'WHERE'), ('IDENTIFIER', 'balance'), ('OPERATOR', '>='), ('NUMBER', '10000'), ('KEYWORD', 'AND'), ('IDENTIFIER', 'currency'), ('OPERATOR', '='), ('STRING', 'USD'), ('KEYWORD', 'AND'), ('IDENTIFIER', 'region'), ('OPERATOR', '='), ('STRING', 'Europe'), ('SEMICOLON', ';'), ('KEYWORD', 'LIMIT'), ('COLON', ':'), ('NUMBER', '15'), ('KEYWORD', 'GENERATE'), ('COLON', ':'), ('KEYWORD', 'PROMPT'), ('COLON', ':'), ('STRING', 'Create summaries of each of the provided high-value accounts in Europe to use in a presentation.')]```

* Output: ```Tokens: [('KEYWORD', 'RETRIEVE'), ('COLON', ':'), ('KEYWORD', 'SOURCE'), ('COLON', ':'), ('STRING', 'FinanceData.csv'), ('KEYWORD', 'QUERY'), ('COLON', ':'), ('KEYWORD', 'SELECT'), ('OPERATOR', '*'), ('KEYWORD', 'FROM'), ('IDENTIFIER', 'accounts'), ('KEYWORD', 'WHERE'), ('IDENTIFIER', 'balance'), ('OPERATOR', '>='), ('NUMBER', '10000'), ('KEYWORD', 'AND'), ('IDENTIFIER', 'currency'), ('OPERATOR', '='), ('STRING', 'USD'), ('KEYWORD', 'AND'), ('IDENTIFIER', 'region'), ('OPERATOR', '='), ('STRING', 'Europe'), ('SEMICOLON', ';'), ('KEYWORD', 'LIMIT'), ('COLON', ':'), ('NUMBER', '15'), ('KEYWORD', 'GENERATE'), ('COLON', ':'), ('KEYWORD', 'PROMPT'), ('COLON', ':'), ('STRING', 'Create summaries of each of the provided high-value accounts in Europe to use in a presentation.')]```

* Program Description: This program contains a more complex SQL query followed by a detailed LLM prompt. We use all token types in this language, and the SQL query makes use of multiple AND keywords, double character operators (which is tokenized via lookahead), and the * operator.

#### Sample Program 4:
* Input Program: ```RETRIEVE:\nSOURCE: "EmployeeRecords.txt"\nQUERY: SELECT employee_id, name FROM employees WHERE age > 30 # ;\nLIMIT: 5\nGENERATE:\nPROMPT: "Create an alphabetical list of employees and generate a unique username for each of them."```

* Expected Result: 
```Lexical error: unrecognized character # at pos 102 Tokens: []```

* Output: 
```Lexical error: unrecognized character # at pos 102 Tokens: []```

* Program Description: This program shows how our lexer handles unrecognized tokens like the "#".

#### Sample Program 5:
* Program: ```RETRIEVE:\nSOURCE: "CustomersDB.json"\nQUERY: SELECT na_me, _email FROM customers WHERE active = "true";\nLIMIT: 10\nGENERATE:\nPROMPT: "Create thank you emails to each active customer for being a valued customer"```

* Expected Result:   
```Lexical error: unrecognized character _ at pos 58 Tokens: []```

* Output:
```Lexical error: unrecognized character _ at pos 58 Tokens: []```

* Program Description: Our program does not support identifiers that begin with "_", but does support identifiers that contain "_". This program is used to demonstrate that our lexer will fail when an identifier starts with an underscore, not when the underscore is within the iden


### 4. Script `run.py`

To run our script, run the following commands:
1. `cd lexer`
2. `python3 run.py`.

This will run our lexer algorithm on our 5 input programs - 2 of which succeed and 3 of which have lexical analysis errors.

This script defines a main function that runs a lexer on several sample input programs. Each program simulates a query with commands like RETRIEVE, QUERY, and GENERATE, using different data sources and prompts. The Lexer tokenizes each input program, and the resulting tokens are printed to the console. If there is an error, the lexer class error handles and prints the message and the position of the erroneous token/character.
