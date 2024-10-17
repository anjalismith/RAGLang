from lexer import Lexer

def main():
    sample_programs = [
        # todo: come up with our own
        ]

    for i, program in enumerate(sample_programs, 1):
        print(f"Running Lexer on Program {i}")
        lexer = Lexer(program)
        tokens = lexer.scan()
        print("Tokens:", tokens)
        print()

if __name__ == "__main__":
    main()
