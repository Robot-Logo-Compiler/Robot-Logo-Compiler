import unittest
from src.logo_parser import parse

class TestParser(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_basic_program_creates_the_correct_tree(self):
        tokens = [('KEYWORD', 'tulosta'), ('PARAMETER', 'Moikka'), ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'oikealle'), ('PARAMETER', '45'), ('KEYWORD', 'vasemmalle'), ('PARAMETER', '90')]
        tree = parse(tokens)
        self.assertEqual("tulosta", tree.root.children[0].keyword)
        self.assertEqual("taakse", tree.root.children[2].keyword)
        self.assertEqual("45", tree.root.children[3].child.value)
        self.assertEqual("90", tree.root.children[4].child.value)

    def test_basic_binary_operatiosn_create_the_correct_tree(self):
        tokens = [('KEYWORD', 'forward'), ('PARAMETER', 1), ('BIN_OP', 'plus'), ('PARAMETER', 5)]
        tree = parse(tokens)
        self.assertEqual("plus", tree.root.children[0].child.operand_type)
        self.assertEqual(1, tree.root.children[0].child.child_one.value)
        self.assertEqual(5, tree.root.children[0].child.child_two.value)

    def test_sqrt_works_on_simple_number_input(self):
        tokens = [('FUNCTION', 'sqrt'), ('PARAMETER', 1)]
        tree = parse(tokens)
        self.assertEqual("sqrt", tree.root.children[0].name)
        self.assertEqual(1, tree.root.children[0].parameters[0].value)

    def test_sqrt_works_on_simple_function_input(self):
        tokens = [('FUNCTION', 'sqrt'), ('FUNCTION', 'sqrt'), ('PARAMETER', 1)]
        tree = parse(tokens)
        self.assertEqual("sqrt", tree.root.children[0].name)
        self.assertEqual(1, tree.root.children[0].parameters[0].parameters[0].value)

    def test_make_function_works(self):
        tokens = [('KEYWORD', 'make'), ('PARAMETER', 'x'), ('PARAMETER', 1)]
        tree = parse(tokens)
        self.assertEqual("x", tree.root.children[0].name.value)

    def test_simple_binary_operation_works(self):
        tokens = [('FUNCTION', 'sqrt'), ('PARAMETER', 1), ("BIN_OP", "plus"), ('PARAMETER', 2)]
        tree = parse(tokens)
        self.assertEqual(1, tree.root.children[0].parameters[0].child_one.value)