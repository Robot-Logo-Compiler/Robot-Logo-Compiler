from sys import argv
from lexer import Lexer
from pathlib import Path

def main():
    lexer = Lexer(openfile())
    tokens = lexer.create_tokens()
    #parsed_tokens = parser.xxx(tokens)
    #code = code_generator.xxx(parsed_tokens)
    writefile(str(tokens).strip('[]'))


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
    f = open("code.java", "a")
    f.write(code)
    f.close()

if __name__ == "__main__":
    main()
