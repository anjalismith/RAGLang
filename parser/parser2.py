from lexer.lexer import Lexer

class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children else []

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.type) + "\n" 
        if self.value:
            ret = "\t" * level + repr(self.type) + ": " + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self):
        try:
            return self.program()
        except SyntaxError as e:
            print(f"Syntax error: {e}")
            return None

    def match(self, expected_type, expected_value=None):
        if self.pos < len(self.tokens):
            token_type, token_value = self.tokens[self.pos]
            if token_type == expected_type and (expected_value is None or token_value == expected_value):
                self.pos += 1
                return token_value
        raise SyntaxError(f"Expected {expected_type} '{expected_value}' at position {self.pos}")

    def program(self):
        node = ASTNode("Program")
        node.children.append(self.r())
        node.children.append(self.q())
        node.children.append(self.g())
        return node

    def r(self):
        # Retrieve Node
        retrieve_node = ASTNode("R")
        self.match("KEYWORD", "RETRIEVE")
        retrieve_node.children.append(ASTNode("Keyword", "RETRIEVE"))
        
        self.match("COLON")
        
        # Source Node
        self.match("KEYWORD", "SOURCE")
        source_node = ASTNode("Source")
        source_node.children.append(ASTNode("Keyword", "SOURCE"))
        
        self.match("COLON")
        
        source_name = self.match("STRING")
        source_node.children.append(ASTNode("String", value=source_name))
        
        retrieve_node.children.append(source_node)
        return retrieve_node

    def q(self):
        query_node = ASTNode("Q")
        self.match("KEYWORD", "QUERY")
        query_node.children.append(ASTNode("Keyword", "QUERY"))
        
        self.match("COLON")
        
        self.match("KEYWORD", "SELECT")
        query_node.children.append(ASTNode("Keyword", "SELECT"))

        a_node = ASTNode("A")
        a_node.children.append(self.a())
        query_node.children.append(a_node)
        
        self.match("KEYWORD", "FROM")
        query_node.children.append(ASTNode("Keyword", "FROM"))
        
        identifier = self.match("IDENTIFIER")
        query_node.children.append(ASTNode("Identifier", value=identifier))
        
        where_node = self.w()
        if where_node:
            query_node.children.append(where_node)
        
        limit_node = self.l()
        if limit_node:
            query_node.children.append(limit_node)
        
        return query_node

    def w(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos][1] == "WHERE":
            where_node = ASTNode("Where")
            self.match("KEYWORD", "WHERE")
            where_node.children.append(ASTNode("Keyword", "WHERE"))
            where_node.children += self.d()
            self.match("SEMICOLON")
            return where_node
        else:
            self.match("SEMICOLON")
            return None

    def l(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos][1] == "LIMIT":
            limit_node = ASTNode("L")
            self.match("KEYWORD", "LIMIT")
            limit_node.children.append(ASTNode("Keyword", "LIMIT"))
            
            self.match("COLON")
            
            number = self.match("NUMBER")
            limit_node.children.append(ASTNode("Number", value=number))
            return limit_node
        return None  # epsilon

    def a(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos][1] == "*":
            self.match("OPERATOR", "*")
            return ASTNode("Operator", value="*")
        else:
            return ASTNode("List", children=self.list())

    def list(self):
        items = [ASTNode("Identifier", value=self.match("IDENTIFIER"))]
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == "COMMA":
            self.match("COMMA")
            items.append(ASTNode("Identifier", value=self.match("IDENTIFIER")))
        return items

    def d(self):
        conditions = [self.condition()]
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in {"AND", "OR"}:
            operator = self.match("KEYWORD")
            operator_node = ASTNode("Keyword", value=operator)
            right_condition = self.condition()
            conditions.append(ASTNode("D", children=[conditions.pop(), operator_node, right_condition]))
        return conditions

    def condition(self):
        condition_node = ASTNode("Condition")
        
        identifier = self.match("IDENTIFIER")
        condition_node.children.append(ASTNode("Identifier", value=identifier))
        
        operator = self.match("OPERATOR")
        condition_node.children.append(ASTNode("Operator", value=operator))
        
        if self.tokens[self.pos][0] == "STRING":
            value = self.match("STRING")
            condition_node.children.append(ASTNode("Value", value=value))
        elif self.tokens[self.pos][0] == "NUMBER":
            value = self.match("NUMBER")
            condition_node.children.append(ASTNode("Value", value=value))
        else:
            raise SyntaxError("Expected STRING or NUMBER in condition")
        
        return condition_node

    def g(self):
        generate_node = ASTNode("G")
        self.match("KEYWORD", "GENERATE")
        generate_node.children.append(ASTNode("Keyword", "GENERATE"))
        
        self.match("COLON")
        
        self.match("KEYWORD", "PROMPT")
        prompt_node = ASTNode("Prompt")
        prompt_node.children.append(ASTNode("Keyword", "PROMPT"))
        
        self.match("COLON")
        
        prompt_string = self.match("STRING")
        prompt_node.children.append(ASTNode("String", value=prompt_string))
        
        generate_node.children.append(prompt_node)
        return generate_node

# Test code
# --------------------- # 
lexer = Lexer("QUERY; SELECT name, age FROM students WHERE age > 18 LIMIT; 10")
l2 = Lexer('RETRIEVE: SOURCE: "SalesDB.json" QUERY: SELECT * FROM sales_data WHERE age > "20" OR time = "2"; LIMIT: 5 GENERATE: PROMPT: "Summarize"')
tokens = l2.scan()
print(tokens)
parser = Parser(tokens)
ast = parser.parse()
print(ast)


