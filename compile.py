from sys import argv
from src.lexer import Lexer
from src.logo_parser import ParserTree
from src.code_generator import Generator
from src.analyzer import Analyzer
from pathlib import Path


def main():
    lexer = Lexer(openfile())
    tokens = lexer.create_tokens()
    parsed_tokens = ParserTree(tokens)
    Analyzer(parsed_tokens)
    generator = Generator(parsed_tokens)
    generator.list_commands()
    generator.generate_code()


def openfile():
    from src.error_handler import FileNumberException
    args = argv[1:]
    if (len(args) > 1) or (len(args) == 0):
        raise FileNumberException(len(args))
        exit()
    try:
        file = Path(args[0]).read_text()
        return file.replace('\n', ' ')
    except OSError:
        print('Could not open file:', file, 'Please provide one file of Logo code as argument.')
        exit()



if __name__ == "__main__":
    main()
