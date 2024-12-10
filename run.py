import sqlite3
from lexer.lexer import Lexer
from parser.parser2 import Parser
from code_generator import CodeGenerator

# 5 input programs
programs = [
    'RETRIEVE: SOURCE: "sales-2024.db" QUERY: SELECT name, email FROM customers WHERE active = "true";\nLIMIT: 10\nGENERATE:\nPROMPT: "Create a different thank you message for each customer."',
    'RETRIEVE: SOURCE: "sales-2024.db" QUERY: SELECT product, total_sales FROM sales_data \nWHERE year = 2023 AND total_sales > 4000 AND region = "North America";\nGENERATE: PROMPT: "Write catchy descriptions of each of our top-selling products in 2023 for North America that we can use on our social media page."',
    'RETRIEVE:\nSOURCE: "sales-2024.db"\nQUERY: SELECT product_name FROM inventory WHERE stock < 25;\nLIMIT: 5\nGENERATE:\nPROMPT: "Create a 2-month marketing campaign to advertise our lowest selling products, which will be 25% off during Black Friday"',
    'RETRIEVE:\nSOURCE: "sales-2024.db"\nQUERY: SELECT product_id FROM sales_data WHERE quantity > 10;\nLIMIT: 5\nGENERATE:\nPROMPT: "Summarize sales data to generate a motivational message that I can use to deliver to our salespeople for their hardwork this quarter."',
    'RETRIEVE:\nSOURCE: "sales-2024.db"\n SELECT customer_id, purchase_amount FROM transactions WHERE purchase_amount > 100 AND loyalty_status = "Gold";\nGENERATE:\nPROMPT: "Summarize high-value transactions"'
]

for i, program in enumerate(programs, 1):
    print(f"\nProcessing RagLang Program {i}:\n{'-' * 40}")
    # Tokenize input
    lexer = Lexer(program)
    tokens = lexer.scan()

    # Parse tokens
    parser = Parser(tokens)
    ast = parser.parse()
    print("AST: ", ast)

    if ast:
        sql_query = CodeGenerator.extract_sql_query(ast)
        prompt_string = CodeGenerator.extract_prompt(ast)
        source = CodeGenerator.extract_source(ast)

        # Execute SQL query on SQLite
        print("\n" + "="*100)
        print("🌟 RAGLANG OUTPUT 🌟")
        try:
            # Connect to SQLite database (assuming CustomersDB.json is a SQLite file)
            conn = sqlite3.connect(source)
            cursor = conn.cursor()

            # Execute query
            cursor.execute(sql_query)
            results = cursor.fetchall()
            
            # Print results
            if results:
                print("Copy and paste the following text into the AI assistant of your choice (e.g., ChatGPT, Claude)")
                print("="*100)
                print()
                print("Please respond to the following prompt using the provided data.")
                print()
                print("Data:")
                for row in results:
                    print("- " + ", ".join(map(str, row)))
                print()
                print("Prompt:", prompt_string)
            else:
                print("="*100+"\n")
                print("No data found in the database:", source)

            conn.close()
        except Exception as e:
            print("="*100+"\n")
            print(f"Error in SQL query {e}")
    else:
        print("Failed to parse input.")
