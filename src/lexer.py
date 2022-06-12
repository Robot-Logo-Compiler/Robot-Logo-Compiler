'''This module splits Logo commands into a list of tokens for the parser'''
from src.logo_keywords import LOGO_KEYWORDS, LOGO_KEYWORDS_BINARY_OPERATIONS, LOGO_KEYWORDS_MATH_FUNCTIONS, LOGO_KEYWORDS_SYMBOLS, LOGO_ALL
from src.error_handler import LexerError

class Lexer:
    ''' This class splits a given Logo code by commands and compares them with a constant keyword list.
    Finally, commands are turned into a list of tokens. '''
    def __init__(self, input_code):
        self.input_code = input_code
        self.keywords = LOGO_KEYWORDS
        self.binary_ops = LOGO_KEYWORDS_BINARY_OPERATIONS
        self.symbols = LOGO_KEYWORDS_SYMBOLS
        self.functions = LOGO_KEYWORDS_MATH_FUNCTIONS

    def create_tokens(self):
        ''' Goes through every word in code. If they are found in KEYWORDS, they are interpreted as
        commands, or otherwise parameters. '''
        token_list = []
        split_list = self.input_code.replace('\n', ' ').replace('(', ' ( ').replace(')', ' ) ').split()

        for element in split_list:
            if element not in self.symbols and element.lower() in self.keywords.keys():
                token_list.append(("KEYWORD", element.lower()))
            elif element in self.binary_ops.keys(): 
                token_list.append(("BIN_OP", self.binary_ops[element]))
            elif element in self.symbols.keys(): 
                token_list.append(("SYMBOL", (self.symbols[element])))
            elif element in self.functions.keys(): 
                token_list.append(("MATH_FUNC", (self.functions[element])))
            else:
                token_list.append(("PARAMETER", element))
        #print(token_list)
        return token_list

    def set_input_code(self, input_code):
        ''' A setter function for input code. '''
        self.input_code = input_code
