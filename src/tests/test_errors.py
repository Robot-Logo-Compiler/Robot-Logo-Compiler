import unittest
from src.logo_parser import parse
from src.analyzer import Analyzer
from compile import openfile
from src.lexer import Lexer

class TestParserTreeErrors(unittest.TestCase):
    def setUp(self):
        tokens1 = [('KEYWORD', 'forward'), ('VARIABLE', 'x')]
        self.parsed_tokens1 = parse(tokens1)

        tokens2 = [('KEYWORD', 'forward'), ('PARAMETER', '"heh')]
        self.parsed_tokens2 = parse(tokens2)

        tokens3 = [('KEYWORD', 'make'), ('PARAMETER', '3'), ('PARAMETER', '"ffff')]
        self.parsed_tokens3 = parse(tokens3)

        tokens4 = [('KEYWORD', 'forward'), ('PARAMETER', '"vg'), ('BIN_OP', 'plus'), ('PARAMETER', '1')]
        self.parsed_tokens4 = parse(tokens4)

        tokens5 = [('KEYWORD', 'forward'), ('PARAMETER', '3'), ('BIN_OP', 'plus'), ('PARAMETER', '"FF')]
        self.parsed_tokens5 = parse(tokens5)

    def test_cant_reference_variable_before_assignment(self):
        with self.assertRaises(SystemExit) as error:
            Analyzer(self.parsed_tokens1)
        self.assertEqual(error.exception.code, "Muuttujaan x viitattiin ennen sen luontia")

    def test_cant_give_function_wrong_parameter_type(self):
        with self.assertRaises(SystemExit) as error:
            Analyzer(self.parsed_tokens2)
        self.assertEqual(error.exception.code, "forward-funktio sai syötteeksi tyypin: str, vaikka se haluaa jotakin, joka palauttaa tyypin: number")
        with self.assertRaises(SystemExit) as error:
            Analyzer(self.parsed_tokens3)
        self.assertEqual(error.exception.code, "make-funktio sai syötteeksi tyypin: number, vaikka se haluaa jotakin, joka palauttaa tyypin: string")

    def test_cant_give_binary_operation_things_that_arent_numbers(self):
        with self.assertRaises(SystemExit) as error:
            Analyzer(self.parsed_tokens4)
        self.assertEqual(error.exception.code, "Laskutoimituksen yhteydessä saa olla vain numeroita. Nyt siellä on jotain muuta myös mukana :(")
        with self.assertRaises(SystemExit) as error:
            Analyzer(self.parsed_tokens5)
        self.assertEqual(error.exception.code, "Laskutoimituksen yhteydessä saa olla vain numeroita. Nyt siellä on jotain muuta myös mukana :(")

class TestFileOpenErrors(unittest.TestCase):
    def setUp(self):
        self.files1 = []
        self.files2 = ["koodi.logo", "koookospahkina.logo"]

    def test_cant_open_without_file_given(self):
        with self.assertRaises(SystemExit) as error:
            openfile(self.files1)
        self.assertEqual(error.exception.code, "Et antanut tiedostoa käännettäväksi.")

    def test_cant_open_with_too_many_files_given(self):
        with self.assertRaises(SystemExit) as error:
            openfile(self.files2)
        self.assertEqual(error.exception.code, "Annoit liian monta tiedostoa käännettäväksi.")

class TestLexerErrors(unittest.TestCase):
    def setUp(self):
        self.lexer1 = Lexer('make "3')
        self.lexer2 = Lexer('make greg 4')

    def test_cant_create_variable_without_enough_information(self):
        with self.assertRaises(SystemExit) as error:
            self.lexer1.create_tokens()
        self.assertEqual(error.exception.code, "Sain käskyksi luoda muuttujan, mutta koodia ei ole riittävästi muuttujan luomiseen")

    def test_cant_create_variable_without_enough_information(self):
        with self.assertRaises(SystemExit) as error:
            self.lexer2.create_tokens()
        self.assertEqual(error.exception.code, 'Sain nimen muuttujalle, mutta nimeämiseen tarvitsen nimen eteen myös heittomerkin eli "\nTee seuraava korjaus: greg -> "greg')
