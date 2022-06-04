from sys import argv
from src.lexer import Lexer
from src.logo_parser import ParserTree
from src.code_generator import Generator
from pathlib import Path

def main():
    lexer = Lexer(openfile())
    tokens = lexer.create_tokens()
    parsed_tokens = ParserTree(tokens)
    Generator(parsed_tokens)


def openfile():
    args = argv[1:]
    if len(args) > 1:
        print('Too many arguments. Please provide one file of Logo code as argument.')
        exit()
    if len(args) == 0:
        print('No file provided as argument. Please provide one file of Logo code as argument.')
        exit()
    try:
        file = Path(args[0]).read_text()
        return file.replace('\n', ' ')
    except OSError:
        print('Could not open file:', file, 'Please provide one file of Logo code as argument.')
        exit()



if __name__ == "__main__":
    main()
