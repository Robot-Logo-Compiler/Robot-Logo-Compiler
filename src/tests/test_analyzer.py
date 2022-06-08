import unittest
from unittest.mock import MagicMock, PropertyMock
from src.analyzer import Analyzer
from src.logo_parser import KeywordNode, CodeNode, ParameterNode
from src.error_handler import SemanticError

class testAnalyzer(unittest.TestCase):

    def test_child_is_string_when_should_be_numeric(self):
        root = CodeNode()
        keynode = KeywordNode("eteen")
        keynode.add_child(ParameterNode('"moi'))
        root.add_child(keynode)
        
        mock_tree = MagicMock()
        type(mock_tree).root = PropertyMock(return_value=root)

        with self.assertRaises(SemanticError):
            Analyzer(mock_tree)


