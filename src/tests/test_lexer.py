import unittest
from src.lexer import Lexer
from pathlib import Path
import unittest, sys, io

class TestLexer(unittest.TestCase):

    ''' Helper function used to load files from testfiles '''
    def load_input_file(self, input_file_path, lines=False):
        try:
            if lines:
                input_file = open(input_file_path, 'r').readlines()
            else:
                input_file = Path(input_file_path).read_text()
        except OSError:
            Exception.os_not_able_to_open_file(input_file_path)

        return input_file

    def setUp(self):
        self.lexer = Lexer("")
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_printing_multiple_strings(self):
        self.lexer.set_input_code('Tulosta "Moikka "moikka')
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'tulosta'), ('PARAMETER', '"Moikka'), ('PARAMETER', '"moikka')]
        self.assertEqual(expected_output, test_input)

    def test_all_finnish_keywords_work_and_is_case_insensitive(self):
        self.lexer.set_input_code("EteEn 5 TaakSe 5 VaSemmalle 5 OiKeaLLE 5 TULOSTA 5")
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'vasemmalle'), ('PARAMETER', '5'), ('KEYWORD', 'oikealle'), ('PARAMETER', '5'), ('KEYWORD', 'tulosta'), ('PARAMETER', '5')]
        self.assertEqual(expected_output, test_input)

    def test_all_english_keywords_work_and_is_case_insensitive(self):
        self.lexer.set_input_code("ForwArd 5 bacK 5 Left 5 riGHT 5 SHOW 5")
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'forward'), ('PARAMETER', '5'), ('KEYWORD', 'back'), ('PARAMETER', '5'), ('KEYWORD', 'left'), ('PARAMETER', '5'), ('KEYWORD', 'right'), ('PARAMETER', '5'), ('KEYWORD', 'show'), ('PARAMETER', '5')]
        self.assertEqual(expected_output, test_input)

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

    def test_all_binary_operations_ignore_spaces(self):
        input_file = self.load_input_file("testfiles/lexer_tests/all_binary_operations_ignore_spaces.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'multiply'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'divide'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'multiply'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'divide'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'multiply'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'divide'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'multiply'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'divide'), ('PARAMETER', '1')]
        self.assertEqual(expected_output, test_input)

    def test_all_keywords_work_with_correct_inputs_FIN(self):
        input_file = self.load_input_file("testfiles/lexer_tests/all_keywords_work_with_correct_inputs_FIN.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'tulosta'), ('PARAMETER', '"Moikka'), ('KEYWORD', 'tulosta'), ('PARAMETER', '123'), ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'oikealle'), ('PARAMETER', '45'), ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'vasemmalle'), ('PARAMETER', '90'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'olkoon'), ('VARIABLE', 'a'), ('PARAMETER', '123'), ('KEYWORD', 'olkoon'), ('VARIABLE', 'b'), ('PARAMETER', 'omena')]
        self.assertEqual(expected_output, test_input)

    def test_all_keywords_work_with_correct_inputs_ENG(self):
        input_file = self.load_input_file("testfiles/lexer_tests/all_keywords_work_with_correct_inputs_FIN.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'tulosta'), ('PARAMETER', '"Moikka'), ('KEYWORD', 'tulosta'), ('PARAMETER', '123'), ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'oikealle'), ('PARAMETER', '45'), ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'vasemmalle'), ('PARAMETER', '90'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'olkoon'), ('VARIABLE', 'a'), ('PARAMETER', '123'), ('KEYWORD', 'olkoon'), ('VARIABLE', 'b'), ('PARAMETER', 'omena')]
        self.assertEqual(expected_output, test_input)

    def test_square_root_function_is_recognized(self):
        self.lexer.set_input_code("show sqrt 4")
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('KEYWORD', 'sqrt'), ('PARAMETER', '4')]
        self.assertEqual(expected_output, test_input)

    def test_parenthesis_in_math_operations(self):
        input_file = self.load_input_file("testfiles/lexer_tests/correct_order_of_operations.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('KEYWORD', 'forward'), ('PARAMETER', '2'), ('BIN_OP', 'plus'), ('PARAMETER', '4'), ('BIN_OP', 'minus'), ('PARAMETER', '3'), ('KEYWORD', 'back'), ('KEYWORD', 'sqrt'), ('PARAMETER', '4'), ('BIN_OP', 'plus'), ('PARAMETER', '3'), ('KEYWORD', 'show'), ('PARAMETER', '"helllo'), ('KEYWORD', 'forward'), ('PARAMETER', '4'), ('BIN_OP', 'multiply'), ('SYMBOL', 'left_paren'), ('PARAMETER', '4'), ('BIN_OP', 'divide'), ('PARAMETER', '2'), ('SYMBOL', 'right_paren'), ('KEYWORD', 'forward'), ('PARAMETER', '4'), ('BIN_OP', 'multiply'), ('PARAMETER', '4'), ('BIN_OP', 'divide'), ('PARAMETER', '2'), ('KEYWORD', 'back'), ('KEYWORD', 'sqrt'), ('PARAMETER', '4'), ('BIN_OP', 'plus'), ('PARAMETER', '3'), ('BIN_OP', 'divide'), ('PARAMETER', '2'), ('KEYWORD', 'forward'), ('KEYWORD', 'sqrt'), ('PARAMETER', '4'), ('BIN_OP', 'plus'), ('PARAMETER', '3'), ('BIN_OP', 'divide'), ('PARAMETER', '2')]
        self.assertEqual(expected_output, test_input)

    def test_parenthesis_work_before_keywords(self):
        input_file = self.load_input_file("testfiles/lexer_tests/parenthesis_work_before_keywords.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('SYMBOL', 'left_paren'), ('KEYWORD', 'show'), ('PARAMETER', '1234'), ('SYMBOL', 'right_paren'), ('SYMBOL', 'left_paren'), ('KEYWORD', 'show'), ('KEYWORD', 'sqrt'), ('PARAMETER', '1234'), ('SYMBOL', 'right_paren')]
        self.assertEqual(expected_output, test_input)

    def test_additive_order_of_operations_correct_order(self):
        input_file = self.load_input_file("testfiles/lexer_tests/additive_order_of_operations_correct_order.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('SYMBOL', 'left_paren'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('SYMBOL', 'right_paren'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('PARAMETER', '3'), ('BIN_OP', 'plus'), ('BIN_OP', 'minus'), ('PARAMETER', '1'), ('KEYWORD', 'show'), ('BIN_OP', 'minus'), ('BIN_OP', 'minus'), ('BIN_OP', 'minus'), ('BIN_OP', 'minus'), ('BIN_OP', 'minus'), ('BIN_OP', 'minus'), ('BIN_OP', 'minus'), ('PARAMETER', '10')]
        self.assertEqual(expected_output, test_input)

    def test_correct_variable_syntax_works(self):
        input_file = self.load_input_file("testfiles/lexer_tests/correct_variable_syntax_works.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'make'), ('VARIABLE', 'a'), ('PARAMETER', '123'), ('KEYWORD', 'tulosta'), ('PARAMETER', '"Moikka'), ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'make'), ('VARIABLE', 'a'), ('PARAMETER', '654'), ('KEYWORD', 'make'), ('VARIABLE', 'b'), ('PARAMETER', '654'), ('KEYWORD', 'tulosta'), ('PARAMETER', '"Moikka')]
        self.assertEqual(expected_output, test_input)

    def test_correct_symbol_table(self):
        input_file = self.load_input_file("testfiles/lexer_tests/correct_symbol_table.logo")
        self.lexer.set_input_code(input_file)
        self.lexer.create_tokens()
        test_input = self.lexer.get_symbol_table()
        expected_output = {'jaakko': '123', 'a': '123', 'b': '123'}
        self.assertEqual(expected_output, test_input)

    # The lexer will delegate the parser to handle these errors
    def test_lexer_passes_binary_operation_edge_cases(self):
        input_file = self.load_input_file("testfiles/lexer_tests/binary_operation_edge_cases.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'show'), ('VARIABLE', 'a'), ('BIN_OP', 'plus'), ('PARAMETER', '3'), ('KEYWORD', 'show'), ('PARAMETER', '3'), ('BIN_OP', 'plus'), ('PARAMETER', '3'), ('KEYWORD', 'show'), ('PARAMETER', '3'), ('BIN_OP', 'plus'), ('PARAMETER', '3'), ('KEYWORD', 'show'), ('PARAMETER', '3'), ('BIN_OP', 'plus'), ('PARAMETER', '3'), ('KEYWORD', 'show'), ('PARAMETER', '"'), ('BIN_OP', 'minus'), ('KEYWORD', 'show'), ('PARAMETER', '"moi'), ('BIN_OP', 'plus'), ('PARAMETER', 'moi'), ('KEYWORD', 'show'), ('BIN_OP', 'minus'), ('KEYWORD', 'show'), ('BIN_OP', 'plus'), ('KEYWORD', 'show'), ('BIN_OP', 'divide'), ('KEYWORD', 'show'), ('BIN_OP', 'multiply')]
        self.assertEqual(expected_output, test_input)


    def test_repeat_is_recognized(self):

        input_file = self.load_input_file("testfiles/lexer_tests/repeat_is_recognized.logo")
        self.lexer.set_input_code(input_file)
        test_input = self.lexer.create_tokens()
        expected_output = [('KEYWORD', 'repeat'), ('PARAMETER', '5'), ('SYMBOL', 'left_sq_bracket'), ('SYMBOL', 'right_sq_bracket'), ('KEYWORD', 'repeat'), ('PARAMETER', '5'), ('SYMBOL', 'right_sq_bracket'), ('SYMBOL', 'left_sq_bracket')]
        self.assertEqual(expected_output, test_input)

    # NOT YET WORKING PROPERLY

    def test_variable_edge_cases(self):
        input_file = self.load_input_file("testfiles/lexer_tests/variable_edge_cases.logo")
        self.lexer.set_input_code(input_file)

        with self.assertRaises(SystemExit) as error:
            self.lexer.create_tokens()

    # NOT YET WORKING PROPERLY

    def test_special_character_edge_cases(self):
        input_file = self.load_input_file("testfiles/lexer_tests/special_character_edge_cases.logo")
        self.lexer.set_input_code(input_file)
        with self.assertRaises(SystemExit) as error:
            self.lexer.create_tokens()

        # input_file = self.load_input_file("testfiles/lexer_tests/special_character_edge_cases.logo", lines=True)
        # edge_case_list = input_file
        # for edge_case in edge_case_list:
        #     self.lexer.set_input_code(edge_case)
        #     with self.assertRaises(SystemExit) as error:
        #         self.lexer.create_tokens()
        #     self.assertIn("Komento eteen haluaa syötteen tyyppiä", self.captured_output.getvalue())

    # NOT YET WORKING PROPERLY

    # def test_redefining_variable_type_gives_error(self):
    #     input_file = self.load_input_file("testfiles/lexer_tests/binary_operation_edge_cases.logo")
    #     self.lexer.set_input_code(input_file)

    #     with self.assertRaises(SystemExit) as error:
    #         self.lexer.create_tokens()
