from curses.ascii import isdigit


class Lexer: 
    def __init__(self, input_code):
        self.input_code = input_code.lower()
    
    KEYWORDS = ['eteen', 'taakse', 'oikealle', 'vasemmalle']
    DIGITS = '0123456789'

    def create_tokens(self):
        token_list = []

        #print("inputcode",self.inputcode)
        
        split_list = [element.lower() for element in self.input_code.split()]
        #print("Split:", split_list)
 
        
        for element in split_list:
            if element in self.KEYWORDS:
                token_list.append(("KEYWORD",element))
            elif isdigit(element):
                token_list.append(("INT", int(element)))
            else:
                print("NOT FOUND ", element)
        return token_list
        
    def set_input_code(self, input_code): 
        self.input_code = input_code.lower()
    

"""
input_code = "Eteen 5 Taakse 5"
lex = Lexer(input_code)
lex.create_tokens()

input_code = "Eteen 5 Taakse5"
lex.set_input_code(input_code)
lex.create_tokens()
"""