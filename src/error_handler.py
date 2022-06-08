def raise_system_exit():
    raise SystemExit(0)
    # pass

class InputFileError():

    #   These messages are only in English, since they are only for the teacher to see
    def too_many_arguments():
        print('Too many arguments. Please provide one file of Logo code as argument.')
        raise_system_exit()

    def no_arguments():
        print('No file provided as argument. Please provide one file of Logo code as argument.')
        raise_system_exit()

    def file_read_error(file):
        print('Could not open file:', file, 'Please provide one file of Logo code as argument.')
        raise_system_exit()

class LexerError():
    def unknown_command(command):
        print('En tunnistanut komentoa: "', command, '". Tarkista, että komento on olemassa ja että se on varmasti kirjoitettu oikein :)')
        # print('I could not recognize the command: ', command, '. Please check that the command is spelled correctly :)')
        raise_system_exit()

class ParserError():
    def parameter_without_command(node):
        print(f"Annoit komennoksi {node.value} joka ei ole komentosana. Unohtuiko sinulta komento?")
        

    def child_is_invalid_type(keyword, input_child, correct_type, invalid_type):

        print('Komento "', keyword, '" haluaa syötteeksi "', correct_type,
                '" mutta sen sijaan komento sai syötteeksi "', invalid_type, '".' )
        print('Pystyisitkö vaihtamaan syötteen "', input_child.return_type(), '" tilalle oikeanlaisen syötteen?')

        # print('The command "', keyword, '" wants to have an input of a "', correct_type,
        #        '" but instead the command received an input of "', invalid_type, '".' )
        # print('Would you please change the input "', input_child, '" into a correct one?')
        raise_system_exit()

class SemanticError(BaseException):
    def __init__(self, type, *args):
        self.type = type
        self.message = self.parse_error(list(args))

    def __str__(self):
        return self.message

    def parse_error(self, args):
        if self.type == "keyword_without_child":
            return self.keyword_without_child[args[0]]
        elif self.type == "child_is_invalid_type":
            return self.child_is_invalid_type(args[0], args[1], args[2], args[3])


    def keyword_without_child(keyword):
        return f"Unohtuiko sinulta parametri komennolta {keyword}?"

    def child_is_invalid_type(self, keyword, parameter, correct_type, invalid_type):
        string = f"""Komento {keyword} haluaa syötteen tyyppiä {correct_type} 
        mutta sen sijaan komento sai syötteen tyyppiä {invalid_type}
        Pystyisitkö vaihtamaan syötteen {parameter} tilalle oikeanlaisen syötteen?"""

        return string