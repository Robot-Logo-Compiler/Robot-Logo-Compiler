import unittest
from src.logo_parser import parse
from src.analyzer import Analyzer

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
        with self.assertRaises(SystemExit) as cm1:
            Analyzer(self.parsed_tokens1)
        self.assertEqual(cm1.exception.code, "Muuttujaan x viitattiin ennen sen luontia")

    def test_cant_give_function_wrong_parameter_type(self):
        with self.assertRaises(SystemExit) as cm2:
            Analyzer(self.parsed_tokens2)
        self.assertEqual(cm2.exception.code, "forward-funktio sai syötteeksi tyypin: str, vaikka se haluaa jotakin, joka palauttaa tyypin: number")
        with self.assertRaises(SystemExit) as cm3:
            Analyzer(self.parsed_tokens3)
        self.assertEqual(cm3.exception.code, "make-funktio sai syötteeksi tyypin: number, vaikka se haluaa jotakin, joka palauttaa tyypin: string")

    def test_cant_give_binary_operation_things_that_arent_numbers(self):
        with self.assertRaises(SystemExit) as cm4:
            Analyzer(self.parsed_tokens4)
        self.assertEqual(cm4.exception.code, "Laskutoimituksen yhteydessä saa olla vain numeroita. Nyt siellä on jotain muuta myös mukana :(")
        with self.assertRaises(SystemExit) as cm5:
            Analyzer(self.parsed_tokens5)
        self.assertEqual(cm5.exception.code, "Laskutoimituksen yhteydessä saa olla vain numeroita. Nyt siellä on jotain muuta myös mukana :(")