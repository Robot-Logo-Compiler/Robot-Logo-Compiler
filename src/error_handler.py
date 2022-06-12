# import sys
# import inspect
'''
As the name suggests, this module handels all of the error messages that the compiler raises.
When SystemExit(0) is called via raise_system_exit(), no tracebacks will be shown and the compiler will stop executing.
The terminal message will only consist of the custom compiler error message specified in this script.
'''

def raise_system_exit():
    '''
    Used for toggling traceback error messages on and off.
    '''
    raise SystemExit(0)
    # pass

class InputFileError():
    '''
    Error handler for file input in compiler.py
    '''
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
    '''
    Error handler for lexer.py
    '''
    def unknown_command(command):
        print('En tunnistanut komentoa: "', command, '". Tarkista, että komento on olemassa ja että se on varmasti kirjoitettu oikein :)')
        # print('I could not recognize the command: ', command, '. Please check that the command is spelled correctly :)')
        raise_system_exit()

class ParserError():
    '''
    Error handler for parser.py
    '''
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

class SemanticException():
    def child_is_invalid_type(self, keyword, parameter, correct_type, invalid_type):
        print(f"""Komento {keyword} haluaa syötteen tyyppiä {correct_type}
        mutta sen sijaan komento sai syötteen tyyppiä {invalid_type}
        Pystyisitkö vaihtamaan syötteen {parameter} tilalle oikeanlaisen syötteen?""")

    def keyword_without_child(keyword):
        print(f"Unohtuiko sinulta parametri komennolta {keyword}?")


class FileException():
    def wrong_number_of_files(amount):
        if amount == 0:
            print("Et antanut tiedostoa käännettäväksi.")
        if amount > 1:
            print("Annoit liian monta tiedostoa käännettäväksi.")

    def os_not_able_to_open_file(path):
        print(f"Käyttöjärjestelmä ei pystynyt avaamaan tiedostoa sijainnissa {path}")
    