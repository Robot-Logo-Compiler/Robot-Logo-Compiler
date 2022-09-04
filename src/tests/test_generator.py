import unittest
from src.code_generator import Generator
from src.logo_parser import parse
from src.analyzer import Analyzer

class TestGenerator(unittest.TestCase):
    def setUp(self):
        symbol_table1 = {}
        parsed_tree1 = parse([('KEYWORD', 'tulosta'), ('PARAMETER', '"moikka'),
        ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '4'),
        ('KEYWORD', 'vasemmalle'), ('PARAMETER', '7'), ('KEYWORD', 'oikealle'), ('PARAMETER', '9')])
        Analyzer(parsed_tree1, symbol_table1)
        self.generator1 = Generator(parsed_tree1, symbol_table1)

        symbol_table2 = {}
        parsed_tree2 = parse([('KEYWORD', 'forward'), ('PARAMETER', '4'), ('KEYWORD', 'left'),
        ('PARAMETER', '55'), ('KEYWORD', 'show'), ('PARAMETER', '"vaarakieli'), ('KEYWORD', 'back'),
        ('PARAMETER', '333'), ('KEYWORD', 'right'), ('PARAMETER', '1')])
        Analyzer(parsed_tree2, symbol_table2)
        self.generator2 = Generator(parsed_tree2, symbol_table2)

        symbol_table3 = {}
        parsed_tree3 = parse([('FUNCTION', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'),
        ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('FUNCTION', 'forward'),
        ('PARAMETER', '2'), ('BIN_OP', 'plus'), ('PARAMETER', '4'), ('BIN_OP', 'minus'), ('PARAMETER', '3'),
        ('FUNCTION', 'back'), ('KEYWORD', 'sqrt'), ('PARAMETER', '4'), ('BIN_OP', 'plus'), ('PARAMETER', '3'),
        ('FUNCTION', 'show'), ('PARAMETER', '"helllo')])
        Analyzer(parsed_tree3, symbol_table3)
        self.generator3 = Generator(parsed_tree3, symbol_table3)

        symbol_table4 = {}
        parsed_tree4 = parse([('KEYWORD', 'make'), ('PARAMETER', '"x'), ('PARAMETER', '1'),
        ('BIN_OP', 'plus'), ('PARAMETER', '4'), ('KEYWORD', 'make'), ('PARAMETER', '"y'), ('VARIABLE', 'x'),
        ('BIN_OP', 'plus'), ('PARAMETER', '5'), ('BIN_OP', 'multiply'), ('PARAMETER', '455'), ('KEYWORD', 'make'),
        ('PARAMETER', '"z'), ('VARIABLE', 'x'), ('BIN_OP', 'plus'), ('VARIABLE', 'y'), ('KEYWORD', 'forward'),
        ('VARIABLE', 'x'), ('BIN_OP', 'plus'), ('VARIABLE', 'z'), ('KEYWORD', 'make'), ('PARAMETER', '"k'),
        ('PARAMETER', '1'), ('KEYWORD', 'make'), ('PARAMETER', '"j'), ('PARAMETER', '"hello')])
        Analyzer(parsed_tree4, symbol_table4)
        self.generator4 = Generator(parsed_tree4, symbol_table4)

    def test_generator_creates_correct_command_list_finnish(self):
        self.generator1.list_commands()
        self.assertEqual(['printToLCD("moikka")','travel(pilot, 5)','travel(pilot, (4)*-1)','rotate(pilot, (7)*-1)','rotate(pilot, 9)'],self.generator1.command_list)

    def test_generator_creates_correct_command_list_english(self):
        self.generator2.list_commands()
        self.assertEqual(['travel(pilot, 4)','rotate(pilot, (55)*-1)','printToLCD("vaarakieli")','travel(pilot, (333)*-1)','rotate(pilot, 1)'],self.generator2.command_list)

    def test_generator_creates_correct_command_list_calculations(self):
        self.generator3.list_commands()
        self.assertEqual(['printToLCD("" + (((1+1)+1)))', 'travel(pilot, ((2+4)-3))', 'travel(pilot, (Math.sqrt((4+3)))*-1)', 'printToLCD("helllo")'],self.generator3.command_list)

    def test_generator_creates_correct_command_list_variables(self):
        self.generator4.list_commands()
        self.assertEqual(['double x=(1+4)', 'double y=(x+(5*455))', 'double z=(x+y)', 'travel(pilot, (x+z))', 'double k=1', 'String j="hello"'],self.generator4.command_list)
