'''Main program. It opens the path given as argument, and calls the different compiler functions'''
from sys import argv
from pathlib import Path
from src.lexer import Lexer
from src.logo_parser import ParserTree
from src.code_generator import Generator
from src.analyzer import Analyzer
from src.error_handler import FileException
from src.parcer import parce

def main():
    '''Main program function. It opens the path given as argument, and calls the different compiler functions'''
    file = openfile(argv[1:])
    if file:
        lexer = Lexer(file)
        tokens = lexer.create_tokens()
        parsed_tokens = parce(tokens)
        Analyzer(parsed_tokens)
        generator = Generator(parsed_tokens)
        generator.list_commands()
        generator.generate_code()

def openfile(args):
    '''
    This method opens the file given as argument and checks its validity. 
    It then returns the file contents as string.
    '''
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
