from lexer.lexer import Lexer

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
    
    def consume(self, expected_type, expected_value=None):
        token = self.tokens[self.current_token_index]
        if token.type == expected_type and (expected_value is None or token.value == expected_value):
            self.current_token_index += 1
            return token
        else:
            raise SyntaxError(f"Expected {expected_type} {expected_value if expected_value else ''} but got {token.type} {token.value}")

    def parse_program(self):
        rqg_node = self.parse_RQG()
        return {"Program": rqg_node}

    def parse_RQG(self):
        r_node = self.parse_R()
        q_node = self.parse_Q()
        g_node = self.parse_G()
        return {"R": r_node, "Q": q_node, "G": g_node}

    def parse_R(self):
        self.consume("Keyword", "RETRIEVE")
        self.consume("Semicolon")
        self.consume("Keyword", "SOURCE")
        self.consume("Semicolon")
        string_token = self.consume("String")
        return {"Retrieve": string_token.value}

    def parse_Q(self):
        self.consume("Keyword", "QUERY")
        self.consume("Semicolon")
        self.consume("Keyword", "SELECT")
        a_node = self.parse_A()
        self.consume("Keyword", "FROM")
        identifier_token = self.consume("Identifier")
        e_node = self.parse_E()
        return {"Query": {"Select": a_node, "From": identifier_token.value, "Where/Limits": e_node}}

    def parse_E(self):
        if self.check("Keyword", "WHERE"):
            return self.parse_W()
        elif self.check("Keyword", "LIMIT"):
            return self.parse_L()
        else:
            return None

    def parse_A(self):
        if self.check("Operator", "*"):
            self.consume("Operator", "*")
            return {"All": "*"}
        else:
            return self.parse_List()

    def parse_List(self):
        identifiers = [self.consume("Identifier").value]
        while self.check("Comma"):
            self.consume("Comma")
            identifiers.append(self.consume("Identifier").value)
        return {"List": identifiers}

    def parse_L(self):
        self.consume("Keyword", "LIMIT")
        self.consume("Semicolon")
        number_token = self.consume("Number")
        return {"Limit": number_token.value}

    def parse_W(self):
        self.consume("Keyword", "WHERE")
        d_node = self.parse_D()
        return {"Where": d_node}

    def parse_D(self):
        conditions = [self.parse_Condition()]
        while self.check("Keyword", "AND") or self.check("Keyword", "OR"):
            operator_token = self.consume("Keyword")
            conditions.append((operator_token.value, self.parse_Condition()))
        return {"Conditions": conditions}

    def parse_Condition(self):
        identifier = self.consume("Identifier").value
        operator = self.consume("Operator").value
        value = self.consume("String" if self.check("String") else "Number").value
        return {"Condition": {"Identifier": identifier, "Operator": operator, "Value": value}}

    def parse_G(self):
        self.consume("Keyword", "GENERATE")
        self.consume("Semicolon")
        self.consume("Keyword", "PROMPT")
        self.consume("Semicolon")
        string_token = self.consume("String")
        return {"Generate": string_token.value}

    def check(self, expected_type, expected_value=None):
        token = self.tokens[self.current_token_index]
        return token.type == expected_type and (expected_value is None or token.value == expected_value)

tokens = [
    Token("Keyword", "RETRIEVE"), Token("Semicolon", ";"), Token("Keyword", "SOURCE"), Token("Semicolon", ";"),
    Token("String", "example_source"), Token("Keyword", "QUERY"), Token("Semicolon", ";"), Token("Keyword", "SELECT"),
    Token("Operator", "*"), Token("Keyword", "FROM"), Token("Identifier", "source_db"), Token("Keyword", "WHERE"),
    Token("Identifier", "status"), Token("Operator", "="), Token("String", "active"), Token("Keyword", "LIMIT"),
    Token("Semicolon", ";"), Token("Number", "10"), Token("Keyword", "GENERATE"), Token("Semicolon", ";"),
    Token("Keyword", "PROMPT"), Token("Semicolon", ";"), Token("String", "Generate report")
]

parser = Parser(tokens)

try:
    ast = parser.parse_program()
    print("Parsing successful.")
except ParserError as e:
    print(f"Parser error: {e}")