from sys import argv
from src.lexer import Lexer
from src.logo_parser import ParserTree
from src.code_generator import Generator
from src.analyzer import Analyzer
from pathlib import Path
from src.logo_parser import parse



def main():
    file = openfile(argv[1:])
    if file:
        lexer = Lexer(file)
        tokens = lexer.create_tokens()
        parsed_tokens = parse(tokens)
        # Analyzer(parsed_tokens)
        generator = Generator(parsed_tokens)
        generator.list_commands()
        generator.generate_code()


def openfile(args):
    from src.error_handler import FileException
    if (len(args) > 1) or (len(args) == 0):
        FileException.wrong_number_of_files(len(args))
        return None
    try:
        file = Path(args[0]).read_text()
        return file
    except OSError:
        FileException.os_not_able_to_open_file(args[0])


if __name__ == "__main__":
    main()
