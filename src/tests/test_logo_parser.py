import unittest
from src.logo_parser import ParserTree

class TestParser(unittest.TestCase):
    def setUp(self):
        tokens = [('KEYWORD', 'tulosta'), ('PARAMETER', '"Moikka'), ('KEYWORD', 'eteen'), ('PARAMETER', '5'), ('KEYWORD', 'taakse'), ('PARAMETER', '5'), ('KEYWORD', 'oikealle'), ('PARAMETER', '45'), ('KEYWORD', 'vasemmalle'), ('PARAMETER', '90')]
        self.tree = ParserTree(tokens)
    
    def test_tree_nodes_have_correct_values(self):
        self.assertEqual(self.tree.root.children[0].keyword,"tulosta")
        self.assertEqual(self.tree.root.children[2].keyword,"taakse")
        self.assertEqual(self.tree.root.children[3].child.value,"45")
        self.assertEqual(self.tree.root.children[4].child.value,"90")