from sys import argv
from lexer import Lexer
from parcer import ParcerTree
from code_generator import Generator
from pathlib import Path

def main():
    lexer = Lexer(openfile())
    tokens = lexer.create_tokens()
    parsed_tokens = ParcerTree(tokens)
    code = Generator(parsed_tokens)
    #writefile(str(tokens).strip('[]'))


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

def writefile(code):
    f = open("code.java", "w")
    f.write(code)
    f.close()

if __name__ == "__main__":
    main()
