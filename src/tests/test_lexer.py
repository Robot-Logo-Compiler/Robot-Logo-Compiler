import unittest
from src.lexer import Lexer
from pathlib import Path

class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer("")
        pass

    def test_all_finnish_keywords_work_and_is_case_insensitive(self):
        self.lexer.set_input_code("EteEn 5 TaakSe 5 VaSemmalle 5 OiKeaLLE 5 TULOSTA 5")
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'vasemmalle'), ('PARAMETER', '5'), ('KEYWORD', 'oikealle'), ('PARAMETER', '5'), ('KEYWORD', 'tulosta'), ('PARAMETER', '5')]
        self.assertEqual(expected_output, test_input)
        pass

    def test_all_english_keywords_work_and_is_case_insensitive(self):
        self.lexer.set_input_code("ForwArd 5 bacK 5 Left 5 riGHT 5 SHOW 5")
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'forward'), ('PARAMETER', '5'), ('KEYWORD', 'back'), ('PARAMETER', '5'), ('KEYWORD', 'left'), ('PARAMETER', '5'), ('KEYWORD', 'right'), ('PARAMETER', '5'), ('KEYWORD', 'show'), ('PARAMETER', '5')]
        self.assertEqual(expected_output, test_input)
        pass

    def test_set_input_code(self):
        self.lexer.set_input_code("MOI")
        self.assertEqual("MOI", self.lexer.input_code)

    def test_all_symbols(self):
        self.lexer.set_input_code("()")
        test_input = self.lexer.create_tokens()
        expected_output = [('SYMBOL', 'left_paren'), ('SYMBOL', 'right_paren')]
        self.assertEqual(expected_output, test_input)

    def test_all_binary_operations(self):
        self.lexer.set_input_code("show 1 + 2 - 3 * 4 / 5")
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '2'), ('BIN_OP', 'minus'), ('PARAMETER', '3'), ('BIN_OP', 'multiply'), ('PARAMETER', '4'), ('BIN_OP', 'divide'), ('PARAMETER', '5')]
        self.assertEqual(expected_output, test_input)

    def test_all_math_functions_and_is_case_insensitive(self):
        self.lexer.set_input_code("show sqrt 4")
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('KEYWORD', 'sqrt'), ('PARAMETER', '4')]
        self.assertEqual(expected_output, test_input)

    def test_all_math_functions_and_is_case_insensitive(self):
        self.lexer.set_input_code("show sqrt 4")
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('KEYWORD', 'sqrt'), ('PARAMETER', '4')]
        self.assertEqual(expected_output, test_input)

    def test_all_binary_operations_ignore_spaces(self): 
        try:
            input_file = Path("testfiles/test9.logo").read_text()    
        except OSError:
            Exception.os_not_able_to_open_file("testfiles/test9.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'multiply'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'divide'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'multiply'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'divide'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'multiply'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'divide'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'multiply'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'divide'), ('PARAMETER', '1')]
        self.assertEqual(expected_output, test_input)