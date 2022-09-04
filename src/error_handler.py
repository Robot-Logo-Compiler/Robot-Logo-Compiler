import sys
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
    # pylint: disable=C0116
    @staticmethod
    def too_many_arguments():
        print('Too many arguments. Please provide one file of Logo code as argument.')
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def no_arguments():
        print('No file provided as argument. Please provide one file of Logo code as argument.')
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def file_read_error(file):
        print('Could not open file:', file, 'Please provide one file of Logo code as argument.')
        raise_system_exit()

class LexerError:
    '''
    Error handler for lexer.py
    '''
    # pylint: disable=C0116
    @staticmethod
    def unknown_command(command):
        print('En tunnistanut komentoa: "', command, '". Tarkista, että komento on olemassa ja että se on varmasti kirjoitettu oikein :)')
        # print('I could not recognize the command: ', command, '. Please check that the command is spelled correctly :)')
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def invalid_special_character_detected(element):
        print("Syötteellä", element, " on kirjaimia, joita en osaa käsitellä :(")
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def variable_assigned_without_a_value(variable_name):
        print("Sain muuttujan nimen, mutta en arvoa muuttujalle")
        print("Antaisitko muuttujalle", variable_name, " myös arvon?")
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def variable_named_without_a_quote_to_indicate_a_variable(variable_name):
        print("Sain nimen muuttujalle, mutta nimeämiseen tarvitsen nimen eteen myös heittomerkin eli \" ")
        print("Tee seuraava korjaus: ", variable_name, "->", '"' + variable_name)
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def variable_name_first_character_is_not_string(variable_name):
        print("Sain nimen muuttujalle, mutta nimen ensimmäinen kirja saa olla vain aakkoskirjain")
        print("Tee seuraava korjaus tälle muuttujalle: ", variable_name)
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def variable_name_contains_special_characters(variable_name):
        print("Sain nimen muuttujalle, mutta nimessä ei saa olla erikoismerkkejä lukuunottamatta ensimmäistä heittomerkkiä \" ")
        print("Tee seuraava korjaus tälle muuttujalle: ", variable_name)
        raise_system_exit()

    @staticmethod
    def variable_name_not_defined():
        print("Sain käskyn luoda muuttujan, mutta en muuttujan nimeä :(")
        raise_system_exit()

    @staticmethod
    def code_is_too_short_for_variable_assignment():
        print("Sain käskyksi luoda muuttujan, mutta koodia ei ole riittävästi muuttujan luomiseen")
        raise_system_exit()

    @staticmethod
    def redefining_variable_value_with_a_different_type_than_previously(variable_name):
        print("Nimesit muuttujan,", variable_name, ", uudeksi arvoksi eri tyypin kuin mitä aikaisemman arvon tyyppi oli :(")
        print("Muuttujien arvon tyyppien pitää pysyä samana!")
        raise_system_exit()


class ParserError:
    '''
    Error handler for parser.py
    '''
    # pylint: disable=C0116
    @staticmethod
    def parameter_without_command(node):
        print(f"Annoit komennoksi {node.value}, joka ei ole komentosana. Unohtuiko sinulta komento?")
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def child_is_invalid_type(keyword, input_child, correct_type, invalid_type):
        print('Komento "', keyword, '" haluaa syötteeksi "', correct_type,
                '" mutta sen sijaan komento sai syötteeksi "', invalid_type, '".' )
        print('Pystyisitkö vaihtamaan syötteen "', input_child.return_type(), '" tilalle oikeanlaisen syötteen?')

        # print('The command "', keyword, '" wants to have an input of a "', correct_type,
        #        '" but instead the command received an input of "', invalid_type, '".' )
        # print('Would you please change the input "', input_child, '" into a correct one?')
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def missing_right_parenthesis(expected_token, actual_token):
        print("Sain", actual_token, "mutta odotin", expected_token)
        print("Löytyi vasempi sulku, mutta eri määrä oikeita sulkuja")
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def found_extra_right_parenthesis():
        print("Löysin ylimääräisen oikean sulun :(")
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def expected_keyword_but_found_something_else(invalid_token):
        print("Odotin avainkomentoa, mutta sain aivan jotain muuta:", invalid_token)
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def expected_parameter_but_found_something_else(invalid_token):
        print("Odotin parametria, mutta sain aivan jotain muuta:", invalid_token)
        raise_system_exit()

class SemanticException:
    # pylint: disable=C0116
    @staticmethod
    def child_is_invalid_type(command):
        print(f"""Komento {command} sai syötteeksi väärän tyypin""")
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def keyword_without_child(keyword):
        print(f"Unohtuiko sinulta parametri komennosta {keyword}?")
        raise_system_exit()

class FileException:
    # pylint: disable=C0116
    @staticmethod
    def wrong_number_of_files(amount):
        if amount == 0:
            print("Et antanut tiedostoa käännettäväksi.")
        if amount > 1:
            print("Annoit liian monta tiedostoa käännettäväksi.")
        raise_system_exit()

    # pylint: disable=C0116
    @staticmethod
    def os_not_able_to_open_file(path):
        print(f"Käyttöjärjestelmä ei pystynyt avaamaan tiedostoa sijainnista {path}")
        raise_system_exit()

class TypeException:
    @staticmethod
    def function_got_wrong_parameter_type(function_name, parameter, expected):
        sys.exit(f"{function_name}-funktio sai syötteeksi tyypin: {parameter}, vaikka se haluaa jotakin, joka palauttaa tyypin: {expected}" )

    @staticmethod
    def binary_operation_something_that_is_not_a_number():
        sys.exit("Laskutoimituksen yhteydessä saa olla vain numeroita. Nyt siellä on jotain muuta myös mukana :(")

    @staticmethod
    def temporary_error():
        print(f"Tuntematon virhe tapahtui")
        raise_system_exit()

    @staticmethod
    def variable_referenced_before_assignement(name):
        sys.exit(f"Muuttujaan {name} viitattiin ennen sen luontia")