'''This module splits Logo commands into a list of tokens for the parser'''
from src.error_handler import LexerError
from src.logo_keywords import LOGO_KEYWORDS, LOGO_KEYWORDS_BINARY_OPERATIONS, LOGO_KEYWORDS_MATH_FUNCTIONS, LOGO_KEYWORDS_SYMBOLS, LOGO_VARIABLES

class Lexer:
    ''' This class splits a given Logo code by commands and compares them with a constant keyword list.
    Finally, commands are turned into a list of tokens. '''
    def __init__(self, input_code):
        self.input_code = input_code
        self.keywords = LOGO_KEYWORDS
        self.binary_ops = LOGO_KEYWORDS_BINARY_OPERATIONS
        self.symbols = LOGO_KEYWORDS_SYMBOLS
        self.functions = LOGO_KEYWORDS_MATH_FUNCTIONS
        self.variables = LOGO_VARIABLES
        self.symbol_table = {}

    @staticmethod
    def create_split_list_from_input_code(input_code):
        ''' Performs all the necessary string replacements from raw input code. '''
        replace_dictionary = {'\n': ' ',
                            '(': ' ( ',
                             ')': ' ) ',
                             '+': ' + ',
                             '-': ' - ',
                             '/': ' / ',
                             '*': ' * '
                             }
        return input_code.translate(str.maketrans(replace_dictionary)).split()

    def create_tokens(self):
        ''' Goes through every word in code. If they are found in KEYWORDS, they are interpreted as
        commands, or otherwise parameters. '''
        token_list = []
        split_list = Lexer.create_split_list_from_input_code(self.input_code)
        skip_count = 0

        for index, element in enumerate(split_list):
            if skip_count != 0:
                skip_count -= 1
                continue

            if element.lower() in self.variables.keys():
                token_list.append(("KEYWORD", element.lower()))

                if index + 2 >= len(split_list) or ":" not in split_list[index + 1]:
                    LexerError.variable_assignment_failed()

                variable_name = str(split_list[index + 1].strip(":"))
                variable_value = split_list[index + 2].strip('"')
                self.symbol_table.update( { variable_name : variable_value })
                token_list.append(("VARIABLE", variable_name))
                token_list.append(("PARAMETER", variable_value))
                skip_count = 2

            elif element not in self.symbols and element.lower() in self.keywords.keys():
                token_list.append(("KEYWORD", element.lower()))
            elif element in self.binary_ops.keys():
                token_list.append(("BIN_OP", self.binary_ops[element]))
            elif element in self.symbols.keys():
                token_list.append(("SYMBOL", (self.symbols[element])))
            elif element in self.functions.keys():
                token_list.append(("MATH_FUNC", (self.functions[element])))
            else:
                token_list.append(("PARAMETER", element))
        print(token_list)
        print(self.symbol_table)
        return token_list

    def set_input_code(self, input_code):
        ''' A setter function for input code. '''
        self.input_code = input_code
