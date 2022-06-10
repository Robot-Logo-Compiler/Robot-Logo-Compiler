import unittest
from unittest.mock import MagicMock, PropertyMock
from src.analyzer import Analyzer
from src.logo_parser import KeywordNode, CodeNode, ParameterNode
from src.error_handler import InvalidChildTypeException

class testAnalyzer(unittest.TestCase):

    def create_tree(self, keynode):
        root = CodeNode()
        root.add_child(keynode)
        mock_tree = MagicMock()
        type(mock_tree).root = PropertyMock(return_value=root)
        return mock_tree

    def test_child_is_string_when_should_be_numeric(self):
        keynode = KeywordNode("eteen")
        keynode.add_child(ParameterNode('"moi'))
        with self.assertRaises(InvalidChildTypeException):
            Analyzer(self.create_tree(keynode))

    def test_missing_quotation_raises_exception(self):
        keynode = KeywordNode("tulosta")
        keynode.add_child(ParameterNode('moi'))
        with self.assertRaises(InvalidChildTypeException):
            Analyzer(self.create_tree(keynode))

    def test_child_is_correct_numeric(self):
        keynode = KeywordNode("eteen")
        keynode.add_child(ParameterNode('5.5'))
        try:
            Analyzer(self.create_tree(keynode))
        except InvalidChildTypeException:
            self.fail("InvalidChildTypeException raised incorrectly")

    def test_show_works_with_strings(self):
        keynode = KeywordNode("tulosta")
        keynode.add_child(ParameterNode('"moi'))
        try:
            Analyzer(self.create_tree(keynode))
        except InvalidChildTypeException:
            self.fail("InvalidChildTypeException raised incorrectly")    

    def test_show_works_with_numbers(self):
        keynode = KeywordNode("tulosta")
        keynode.add_child(ParameterNode('5'))
        try:
            Analyzer(self.create_tree(keynode))
        except InvalidChildTypeException:
            self.fail("InvalidChildTypeException raised incorrectly")


            


