class Lexer: 
    def __init__(self, input_code):
        self.input_code = input_code.lower()
    
    KEYWORDS = ['eteen', 'taakse', 'oikealle', 'vasemmalle', 'show']

    def create_tokens(self):
        token_list = []
    
        split_list = [element.lower() for element in self.input_code.split()]
        # print("Split:", split_list)
        
        for index, element in enumerate(split_list):
            if element in self.KEYWORDS:
                token_list.append(("KEYWORD",element))                
            elif split_list[index-1] == "show": 
                token_list.append(("STRING", str(split_list[index])))
            elif element.isdigit():
                token_list.append(("INT", int(element)))
            else:
                print("NOT FOUND ", element)
        return token_list
        
    def set_input_code(self, input_code): 
        self.input_code = input_code.lower()
    


"""
input_code = "Eteen 5 Taakse 5 Show 555 Show lkajsdlk5fjalkdsj"
lex = Lexer(input_code)
print(lex.create_tokens())

input_code = "Eteen 5 Taakse5"
lex.set_input_code(input_code)
lex.create_tokens()
"""