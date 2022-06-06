from src.logo_keywords import LOGO_KEYWORDS

class Lexer: 
    def __init__(self, input_code):
        self.input_code = input_code
        self.KEYWORDS = LOGO_KEYWORDS

    def create_tokens(self):
        token_list = []

        #print("inputcode",self.input_code)
        
        split_list = [element for element in self.input_code.split()]
        #print("Split:", split_list)
 
        
        previous = ''
        for element in split_list:
            if element.lower() in self.KEYWORDS.keys():
                token_list.append(("KEYWORD",element.lower()))
            elif element.isnumeric():
                if(self.KEYWORDS.get(previous.lower()) == 'number'):
                    token_list.append(("PARAMETER", int(element)))
                else:
                    print(f"{element} given as parameter for command {previous} that does not take numeric parameter")
            elif(element[0]=='"'):
                if(self.KEYWORDS.get(previous.lower()) == 'string'):
                    token_list.append(("PARAMETER", element[1:]))
                else:
                    print(f"{element} given as parameter for command {previous} that does not take string parameter")    
            else:
                print("NOT FOUND ", element)
            previous = element
        #print(token_list)
        return token_list
        
    def set_input_code(self, input_code): 
        self.input_code = input_code
    

"""
input_code = "Eteen 5 Taakse 5"
lex = Lexer(input_code)
lex.create_tokens()

input_code = "Eteen 5 Taakse5"
lex.set_input_code(input_code)
lex.create_tokens()
"""
