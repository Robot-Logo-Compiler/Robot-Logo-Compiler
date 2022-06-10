import unittest
from src.code_generator import Generator

class StubTree:
    def __init__(self):
        self.root = StubRoot()
        #print(self.root.children)

class StubRoot:
    def __init__(self):
        self.children = []
        keyword_parameter_list = [('tulosta','"moikka'),('eteen','5'),('taakse','4'),('vasemmalle','7'),('oikealle','9')]
        for pair in keyword_parameter_list:
            self.children.append(StubKeywordNode(pair[0], pair[1]))

class StubKeywordNode:
    def __init__(self, keyword, parameter):
        self.keyword = keyword
        self.child = StubParameterNode(parameter)
        

class StubParameterNode:
    def __init__(self, parameter):
        self.value = parameter
        

class TestGenerator(unittest.TestCase): # Tämä testiluokka on väliaikainen ja on tarkoitus korvata testeillä koodigeneraattorille
    def setUp(self):
        self.generator = Generator(StubTree())

    def test_generator_creates_correct_command_list(self):
        self.generator.list_commands()
        self.assertEqual(['printToLCD("moikka")','moveForward(5)','moveBackward(4)','rotate(-7)','rotate(9)'],self.generator.command_list)
