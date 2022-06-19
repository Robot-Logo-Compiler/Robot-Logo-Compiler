import unittest
from src.code_generator import Generator

class StubTree:
    def __init__(self, parameter_list):
        self.root = StubRoot(parameter_list)

class StubRoot:
    def __init__(self, parameter_list):
        self.children = []
        keyword_parameter_list = parameter_list
        for pair in keyword_parameter_list:
            self.children.append(StubKeywordNode(pair[0], pair[1]))

class StubKeywordNode:
    def __init__(self, keyword, parameter):
        self.keyword = keyword
        self.child = StubParameterNode(parameter)
        

class StubParameterNode:
    def __init__(self, parameter):
        self.value = parameter
        

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator(StubTree([('tulosta','"moikka'),('eteen','5'),('taakse','4'),('vasemmalle','7'),('oikealle','9')]))
        self.generator2 = Generator(StubTree([('forward','4'),('left','55'),('show','"vaarakieli'),('back','333'),('right','1')]))

    def test_generator_creates_correct_command_list_finnish(self):
        self.generator.list_commands()
        self.assertEqual(['printToLCD("moikka")','travel(5)','travel(-4)','rotate(-7)','rotate(9)'],self.generator.command_list)

    def test_generator_creates_correct_command_list_english(self):
        self.generator2.list_commands()
        self.assertEqual(['travel(4)','rotate(-55)','printToLCD("vaarakieli")','travel(-333)','rotate(1)'],self.generator2.command_list)
