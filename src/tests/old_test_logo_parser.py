import unittest
from src.logo_parser import ParserTree

class TestParser(unittest.TestCase):
    def setUp(self):
        tokens = [('KEYWORD', 'tulosta'), ('PARAMETER', '"Moikka'), ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'oikealle'), ('PARAMETER', '45'), ('KEYWORD', 'vasemmalle'), ('PARAMETER', '90')]
        self.tree = ParserTree(tokens)
    
    def test_tree_nodes_have_correct_values(self):
        self.assertEqual("tulosta", self.tree.root.children[0].keyword)
        self.assertEqual("taakse", self.tree.root.children[2].keyword)
        self.assertEqual("45", self.tree.root.children[3].child.value)
        self.assertEqual("90", self.tree.root.children[4].child.value)

    def test_parser_gives_error_on_wrong_input(self):
        tokens2 = [('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'oikealle'), ('PARAMETER', '45')]
        self.assertRaises(TypeError, ParserTree(tokens2))