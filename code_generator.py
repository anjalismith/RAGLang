from parser.parser2 import ASTNode

class CodeGenerator:
    """A class responsible for generating code and extracting information from an Abstract Syntax Tree (AST)."""

    @staticmethod
    def extract_sql_query(ast):
        """
        Extracts the SQL query from the AST, including the LIMIT clause and appends a semicolon.
        :param ast: Root ASTNode object representing the parsed input.
        :return: A string representing the SQL query.
        """
        query_parts = []

        def traverse(node):
            if node.type == "Keyword" and node.value == "SELECT":
                query_parts.append("SELECT")
            elif node.type in {"Identifier", "Operator", "Value"}:
                query_parts.append(node.value)
            elif node.type == "Keyword" and node.value in {"FROM", "WHERE", "LIMIT", "AND", "OR"}:
                query_parts.append(node.value)
            elif node.type == "List":
                query_parts.append(", ".join(child.value for child in node.children))
            elif node.type == "Number" and "LIMIT" in query_parts:  # Handle LIMIT value
                query_parts.append(node.value)
            elif node.type == "D":  # Condition
                traverse(node.children[0])  # Left operand
                query_parts.append(node.children[1].value)  # Operator
                traverse(node.children[2])  # Right operand

            for child in node.children:
                traverse(child)

        traverse(ast)
        query = " ".join(query_parts).strip()
        return f"{query};"  # Ensure the query ends with a semicolon


    @staticmethod
    def extract_prompt(ast):
        """
        Extracts the GENERATE prompt string from the AST.
        :param ast: Root ASTNode object representing the parsed input.
        :return: A string representing the prompt, or None if not found.
        """
        def traverse(node):
            if node.type == "Prompt":
                for child in node.children:
                    if child.type == "String":
                        return child.value
            for child in node.children:
                result = traverse(child)
                if result:
                    return result
            return None

        return traverse(ast)
