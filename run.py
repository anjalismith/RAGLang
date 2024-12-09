import sqlite3
from lexer.lexer import Lexer
from parser.parser2 import Parser
from code_generator import CodeGenerator

# Example input
input_code = 'RETRIEVE: SOURCE: "CustomersDB.json" QUERY: SELECT name, email FROM customers WHERE active = "true";\nLIMIT: 10\nGENERATE:\nPROMPT: "Create thank you emails to each active customer."'

# Tokenize input
lexer = Lexer(input_code)
tokens = lexer.scan()

# Parse tokens
parser = Parser(tokens)
ast = parser.parse()

# Generate code or extract details
if ast:
    print(ast)
    sql_query = CodeGenerator.extract_sql_query(ast)
    prompt_string = CodeGenerator.extract_prompt(ast)

    print("SQL Query:", sql_query)
    print("Prompt String:", prompt_string)

    # Execute SQL query on SQLite
    try:
        # Connect to SQLite database (assuming CustomersDB.json is a SQLite file)
        conn = sqlite3.connect('sample.db')  # or your actual database filename
        cursor = conn.cursor()

        # Execute query
        cursor.execute(sql_query)
        results = cursor.fetchall()

        # Print results
        if results:
            print("Query Results:")
            for row in results:
                print(row)
        else:
            print("No results found.")

        conn.close()
    except Exception as e:
        print(f"Error executing SQL query: {e}")
else:
    print("Failed to parse input.")
