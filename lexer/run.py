from lexer import Lexer

def main():
    sample_programs = [
    'RETRIEVE:\nSOURCE: "SalesDB.json"\nQUERY: SELECT product, total_sales FROM sales_data WHERE year = "2023" AND region = "North America";\nLIMIT: 5\nGENERATE:\nPROMPT: "Summarize the top-performing products in a brief report highlighting key sales figures and top products"\n',
    'RETRIEVE:\nSOURCE: "InventoryDB.csv"\nQUERY: SELECT product_name, stock FROM inventory WHERE stock < 50;\nLIMIT: 20\nGENERATE:\nPROMPT: "Create a social media caption advertising these products which have low stock levels.',
    'RETRIEVE:\nSOURCE: "FinanceData.csv"\nQUERY: SELECT * FROM accounts WHERE balance >= 10000 AND currency = "USD" AND region = "Europe";\nLIMIT: 15\nGENERATE:\nPROMPT: "Create summaries of each of the provided high-value accounts in Europe to use in a presentation."',
    'RETRIEVE:\nSOURCE: "EmployeeRecords.txt"\nQUERY: SELECT employee_id, name FROM employees WHERE age > 30 # ;\nLIMIT: 5\nGENERATE:\nPROMPT: "Create an alphabetical list of employees and generate a unique username for each of them."',
    'RETRIEVE:\nSOURCE: "CustomersDB.json"\nQUERY: SELECT na_me, _email FROM customers WHERE active = "true";\nLIMIT: 10\nGENERATE:\nPROMPT: "Create thank you emails to each active customer for being a valued customer"'
    ]

    for i, program in enumerate(sample_programs, 1):
        print(f"Running Lexer on Program {i}")
        lexer = Lexer(program)
        tokens = lexer.scan()
        print("Tokens:", tokens)
        print()

if __name__ == "__main__":
    main()
