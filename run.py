from lexer.lexer import Lexer
from parser.parser2 import Parser
from code_generator import CodeGenerator

# Example input
input_code = 'RETRIEVE: SOURCE: "SalesDB.json" QUERY: SELECT * FROM sales_data WHERE age > "20" OR time = "2"; LIMIT: 5 GENERATE: PROMPT: "Summarize the results"'

# Tokenize input
lexer = Lexer(input_code)
tokens = lexer.scan()

# Parse tokens
parser = Parser(tokens)
ast = parser.parse()

# Generate code or extract details
if ast:
    sql_query = CodeGenerator.extract_sql_query(ast)
    prompt_string = CodeGenerator.extract_prompt(ast)

    print("SQL Query:", sql_query)
    print("Prompt String:", prompt_string)
else:
    print("Failed to parse input.")
