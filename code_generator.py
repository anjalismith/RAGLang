from parser.parser2 import ASTNode

class CodeGenerator:
    """A class responsible for generating code and extracting information from an Abstract Syntax Tree (AST)."""

    @staticmethod
    def extract_sql_query(ast):
        query_parts = []

        def traverse(node):
            # Handle SELECT keyword
            if node.type == "Keyword" and node.value == "SELECT":
                query_parts.append("SELECT")
                for child in node.children:
                    traverse(child)
            # Handle column names (List node) within the SELECT clause
            elif node.type == "List":
                # Join the column values with commas and append to query_parts
                column_values = [child.value for child in node.children if child.type == "Identifier"]
                query_parts.append(", ".join(column_values))
            # Handle other nodes like FROM, WHERE, LIMIT, etc.
            elif node.type in {"Identifier", "Operator", "Value"}:
                if node.type == "Value" and not (node.value.replace('.', '', 1).isdigit() or node.value.lstrip('-').replace('.', '', 1).isdigit()) and not (node.value == "true" or node.value == "false"):
                        query_parts.append(f'"{node.value}"')
                else:
                    query_parts.append(node.value)
            elif node.type == "Keyword" and node.value in {"FROM", "WHERE", "LIMIT", "AND", "OR"}:
                query_parts.append(node.value)
                for child in node.children:
                    traverse(child)
            elif node.type == "Number" and "LIMIT" in query_parts:  # Handle LIMIT value
                query_parts.append(node.value)
                for child in node.children:
                    traverse(child)
            elif node.type == "D":  # Condition
                traverse(node.children[0])  # Left operand
                query_parts.append(node.children[1].value)  # Operator
                traverse(node.children[2])  # Right operand
            else:
                # Traverse children nodes
                for child in node.children:
                    traverse(child)

        traverse(ast)

        # Print query parts for debugging
        print(f"Query parts: {query_parts}")  # Print the full list of query parts before joining

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
    
    @staticmethod
    def extract_source(ast):
        """
        Extracts the database name from the AST.
        :param ast: Root ASTNode object representing the parsed input.
        :return: The database name
        """
        def traverse(node):
            if node.type == "Source":
                for child in node.children:
                    if child.type == "String":
                        return child.value
            else:
                for child in node.children:
                    result = traverse(child)
                    if result:
                        return result
            return None

        return traverse(ast)
