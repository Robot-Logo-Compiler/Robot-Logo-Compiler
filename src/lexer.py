'''This module splits Logo commands into a list of tokens for the parser'''

from src.logo_keywords import LOGO_KEYWORDS
#from src.error_handler import LexerError

class Lexer:
    ''' This class splits a given Logo code by commands and compares them with a constant keyword list.
    Finally, commands are turned into a list of tokens. '''

    def __init__(self, input_code):
        self.input_code = input_code
        self.KEYWORDS = LOGO_KEYWORDS

    def create_tokens(self):
        ''' Goes through every word in code. If they are found in KEYWORDS, they are interpreted as
        commands, or otherwise parameters. '''
        token_list = []

        #print("inputcode",self.input_code)

        split_list = self.input_code.replace('\n', ' ').replace('(', ' ( ').replace(')', ' ) ').split()
        # print("Split:", split_list)
        
        #previous = ''
        for element in split_list:
            if element.lower() in self.KEYWORDS.keys():
                token_list.append(("KEYWORD",element.lower()))
            else:
                token_list.append(("PARAMETER", element))

        #print(token_list)
        return token_list

    def set_input_code(self, input_code):
        ''' A setter function for input code. '''
        self.input_code = input_code

