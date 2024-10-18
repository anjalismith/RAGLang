class Lexer:
    def __init__(self, input_program):
        self.input_program = input_program

    def scan(self):
        state = "START"
        tokens = []
        curr_token = ""
        pos = 0
        
        while pos < len(self.input_program):
            char = self.input_program[pos]

            if state == "START":
                if char.isalpha():
                    state = "IDENTIFIER"
                    curr_token += char
                elif char.isdigit():
                    state = "NUMBER"
                    curr_token += char
                elif char == ";":
                    tokens.append(("SEMICOLON", char))
                elif char == ":":
                    tokens.append(("COLON", char))
                elif char == ",":
                    tokens.append(("COMMA", char))
                elif char in "=<>*!":
                    curr_token += char
                    state = "OPERATOR"
                elif char == '"':
                    state = "STRING"
                    curr_token = ""
                elif char in (' ', '\t', '\n'):
                    pass
                else:
                    print(f"Lexical error: unrecognized character {char} at pos {pos}")
                    return []
                
            elif state == "IDENTIFIER":
                if char.isalnum() or char == "_":
                    curr_token += char
                else:
                    if curr_token in {"RETRIEVE", "GENERATE", "SELECT", "FROM", "WHERE", "LIMIT", "AND", "OR", "QUERY", "PROMPT", "SOURCE"}:
                        tokens.append(("KEYWORD", curr_token))
                    else:
                        tokens.append(("IDENTIFIER", curr_token))
                    curr_token = ""
                    state = "START"
                    continue

            elif state == "NUMBER":
                if char.isdigit():
                    curr_token += char
                else:
                    tokens.append(("NUMBER", curr_token))
                    curr_token = ""
                    state = "START"
                    continue

            elif state == "OPERATOR":
                if curr_token == "=":
                    tokens.append(("OPERATOR", "="))
                    curr_token = ""
                    state = "START"
                    continue
                if curr_token == "!":
                    if char == "=":
                        tokens.append(("OPERATOR", "!="))
                        curr_token = ""
                        state = "START"
                        pos += 1
                        continue
                    else:
                        print(f"Lexical error: unrecognized token {curr_token} at pos {pos}")
                        return []
                elif curr_token == "<":
                    if char == "=":
                        tokens.append(("OPERATOR", "<="))
                        curr_token = ""
                        state = "START"
                        pos += 1
                        continue
                    else:
                        tokens.append(("OPERATOR", "<"))
                        curr_token = ""
                        state = "START"
                        continue
                elif curr_token == ">":
                    if char == "=":
                        tokens.append(("OPERATOR", ">="))
                        curr_token = ""
                        state = "START"
                        pos += 1
                        continue
                    else:
                        tokens.append(("OPERATOR", ">"))
                        curr_token = ""
                        state = "START"
                        continue
                elif curr_token == "*":
                    tokens.append(("OPERATOR", "*"))
                    curr_token = ""
                    state = "START"
                    continue
                else:
                    print(f"Lexical error: unrecognized character {char} at pos {pos}")
                    return []

            elif state == "STRING":
                if char == '"':
                    tokens.append(("STRING", curr_token))
                    curr_token = ""
                    state = "START"
                else:
                    curr_token += char
            pos += 1
        
        if state == "START":
            return tokens

        if state == "IDENTIFIER":
            if curr_token in {"RETRIEVE", "GENERATE", "SELECT", "FROM", "WHERE", "LIMIT", "AND", "OR", "SOURCE", "QUERY", "PROMPT", "SOURCE"}:
                tokens.append(("KEYWORD", curr_token))
            else:
                tokens.append(("IDENTIFIER", curr_token))
        elif state == "NUMBER":
            tokens.append(("NUMBER", curr_token))
    
        elif state == "OPERATOR":
            if curr_token == "<":
                tokens.append(("OPERATOR", "<"))
            elif curr_token == ">":
                tokens.append(("OPERATOR", ">"))
            elif curr_token == "*":
                tokens.append(("OPERATOR", "*"))
            else:
                print(f"Lexical error: unrecognized character {curr_token} at pos {pos - 1}")
                return []
        elif state == "STRING":
            print(f"Lexical error: unterminated string literal '{curr_token}'")
            return []
        else:
            print(f"Lexical error: unrecognized character {curr_token} at pos {pos - 1}")
            return []

        return tokens