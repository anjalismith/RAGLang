from lexer.lexer import Lexer
from parser.parser2 import Parser


programs = [
    'RETRIEVE:\nSOURCE: "SalesDB.json"\nQUERY: SELECT product, total_sales FROM sales_data WHERE year = "2023" AND region = "North America";\nLIMIT: 5\nGENERATE:\nPROMPT: "Summarize the top-performing products in a brief report highlighting key sales figures and top products"',
    'RETRIEVE:\nSOURCE: "InventoryDB.json"\nQUERY: SELECT * FROM products WHERE stock > 50 AND category = "electronics";\nLIMIT: 20\nGENERATE:\nPROMPT: "List all products with sufficient stock and catchy slogans for each product that we can use on our company social media"',
    'RETRIEVE:\nSOURCE: "Sales.json"\nQUERY: SELECT product_id FROM sales_data WHERE quantity > 10\nLIMIT: 5\nGENERATE:\nPROMPT: "Summarize sales data to generate a motivational message that I can use to deliver to our salespeople for their hardwork this quarter."',
    'RETRIEVE\nSOURCE: "Analytics.json"\nQUERY: SELECT region FROM demographics WHERE age > 18;\nLIMIT: 10\nGENERATE:\nPROMPT: "Provide a summary of regional demographics and turn it into an abstract for our report"',
    'RETRIEVE:\nSOURCE: "CustomerDB.json"\n SELECT customer_id, purchase_amount FROM transactions WHERE purchase_amount > 100 AND loyalty_status = "Gold";\nGENERATE:\nPROMPT: "Summarize high-value transactions"'
]

for i, program in enumerate(programs, 1):
    print(f"\nProcessing Program {i}:\n{'-' * 40}")
    
    lexer = Lexer(program)
    tokens = lexer.scan() 
    print("Tokens:", tokens)
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    print("AST:", ast)
