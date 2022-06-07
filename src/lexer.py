from src.logo_keywords import LOGO_KEYWORDS
from src.error_handler import LexerError
class Lexer:
    def __init__(self, input_code):
        self.input_code = input_code
        self.KEYWORDS = LOGO_KEYWORDS

    def create_tokens(self):
        token_list = []

        #print("inputcode",self.input_code)

        split_list = [element for element in self.input_code.split()]
        #print("Split:", split_list)


        #previous = ''
        for element in split_list:
            if element.lower() in self.KEYWORDS.keys():
                token_list.append(("KEYWORD",element.lower()))
            else:
                token_list.append(("PARAMETER", element))

        #print(token_list)
        return token_list

    def set_input_code(self, input_code):
        self.input_code = input_code
