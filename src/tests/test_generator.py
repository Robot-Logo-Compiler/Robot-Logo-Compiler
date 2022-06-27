import unittest
from src.code_generator import Generator
from src.logo_parser import parse

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator(parse([('KEYWORD', 'tulosta'), ('PARAMETER', '"moikka'),
        ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '4'),
        ('KEYWORD', 'vasemmalle'), ('PARAMETER', '7'), ('KEYWORD', 'oikealle'), ('PARAMETER', '9')]))

        self.generator2 = Generator(parse([('KEYWORD', 'forward'), ('PARAMETER', '4'), ('KEYWORD', 'left'),
        ('PARAMETER', '55'), ('KEYWORD', 'show'), ('PARAMETER', '"vaarakieli'), ('KEYWORD', 'back'),
        ('PARAMETER', '333'), ('KEYWORD', 'right'), ('PARAMETER', '1')]))

        self.generator3 = Generator(parse([('KEYWORD', 'show'), ('PARAMETER', '1'), ('BIN_OP', 'plus'),
        ('PARAMETER', '1'), ('BIN_OP', 'plus'), ('PARAMETER', '1'), ('KEYWORD', 'forward'),
        ('PARAMETER', '2'), ('BIN_OP', 'plus'), ('PARAMETER', '4'), ('BIN_OP', 'minus'), ('PARAMETER', '3'),
        ('KEYWORD', 'back'), ('KEYWORD', 'sqrt'), ('PARAMETER', '4'), ('BIN_OP', 'plus'), ('PARAMETER', '3'),
        ('KEYWORD', 'show'), ('PARAMETER', '"helllo')]))

    def test_generator_creates_correct_command_list_finnish(self):
        self.generator.list_commands()
        self.assertEqual(['printToLCD("moikka")','travel(pilot, 5)','travel(pilot, (4)*-1)','rotate(pilot, (7)*-1)','rotate(pilot, 9)'],self.generator.command_list)

    def test_generator_creates_correct_command_list_english(self):
        self.generator2.list_commands()
        self.assertEqual(['travel(pilot, 4)','rotate(pilot, (55)*-1)','printToLCD("vaarakieli")','travel(pilot, (333)*-1)','rotate(pilot, 1)'],self.generator2.command_list)

    def test_generator_creates_correct_command_list_calculations(self):
        self.generator3.list_commands()
        self.assertEqual(['printToLCD("" + (((1+1)+1)))', 'travel(pilot, ((2+4)-3))', 'travel(pilot, (Math.sqrt((4+3)))*-1)', 'printToLCD("helllo")'],self.generator3.command_list)
