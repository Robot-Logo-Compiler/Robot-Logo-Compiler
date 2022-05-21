class Lexer: 
    def __init__(self, inputcode):
        self.inputcode = inputcode.lower()
    
    KEYWORDS = ['eteen', 'taakse', 'oikealle', 'vasemmalle']
    DIGITS = '0123456789'

    def create_tokens(self):
        token_list = []

        print("inputcode",self.inputcode)
        
        split_list = [element.lower() for element in self.inputcode.split()]
        print("Split:", split_list)
        
        for element in split_list:
            if element in self.KEYWORDS:
                token_list.append(("KEYWORD",element))
            elif element in self.DIGITS:
                token_list.append(("INT", element))
            else:
                print("NOT FOUND ", element)
        print("TOKENS:",token_list)
        
    def set_inputcode(self, inputcode): 
        self.inputcode = inputcode.lower()
    

"""
inputcode = "Eteen 5 Taakse 5"
lex = Lexer(inputcode)
lex.create_tokens()

inputcode = "Eteen 5 Taakse5"
lex.set_inputcode(inputcode)
lex.create_tokens()
"""