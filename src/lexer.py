'''This module splits Logo commands into a list of tokens for the parser'''
import re
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
                              '[': ' [ ',
                              ']': ' ] ',
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

            elif element.lower() in self.variables.keys():
                token_list.append(("KEYWORD", element.lower()))

                if index + 2 >= len(split_list):
                    LexerError.code_is_too_short_for_variable_assignment()

                variable_name = Lexer.check_variable_name_for_errors(split_list[index + 1])
                variable_value = split_list[index + 2]

                token_list.append(("PARAMETER", variable_name))

                if ":" in variable_value[0]:
                    token_list.append(("VARIABLE", variable_value.strip(":")))
                else:
                    token_list.append(("PARAMETER", variable_value))

                skip_count = 2

            elif ":" in element[0]:
                token_list.append(("VARIABLE", element.strip(":")))
            elif element not in self.symbols and element.lower() in self.keywords.keys():
                token_list.append(("KEYWORD", element.lower()))
            elif element in self.binary_ops.keys():
                token_list.append(("BIN_OP", self.binary_ops[element]))
            elif element in self.symbols.keys():
                token_list.append(("SYMBOL", (self.symbols[element])))
            elif element in self.functions.keys():
                token_list.append(("MATH_FUNC", (self.functions[element])))
            else:
                if ":" in element[0]:
                    token_list.append(("VARIABLE", element.strip(":")))
                else:
                    token_list.append(("PARAMETER", element))

        # Prints
        # for i in token_list:
        #     print(i)
        # print(token_list)
        return token_list

    @staticmethod
    def check_variable_name_for_errors(variable_name):
        ''' Provides error checking when naming a variable '''

        if variable_name in LOGO_KEYWORDS or variable_name in LOGO_VARIABLES:
            LexerError.variable_name_not_defined()

        if  '"' not in variable_name[0]:
            LexerError.variable_named_without_a_quote_to_indicate_a_variable(variable_name)

        return variable_name

    def set_input_code(self, input_code):
        ''' A setter function for input code. '''
        self.input_code = input_code

    def get_symbol_table(self):
        return self.symbol_table

