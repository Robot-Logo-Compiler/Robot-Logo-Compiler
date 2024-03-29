import unittest, sys, io
from unittest.mock import MagicMock, PropertyMock
from src.analyzer import Analyzer
from src.logo_parser import KeywordNode, CodeNode, ParameterNode

class testAnalyzer(unittest.TestCase):
    def setUp(self):
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__


    def create_tree_with_one_command(self, keyword, parameter):
        keynode = KeywordNode(keyword)
        keynode.add_child(ParameterNode(parameter))
        root = CodeNode()
        root.add_child(keynode)
        mock_tree = MagicMock()
        type(mock_tree).root = PropertyMock(return_value=root)
        return mock_tree


    def test_child_is_string_when_should_be_numeric(self):
        with self.assertRaises(SystemExit) as error:
            Analyzer(self.create_tree_with_one_command("eteen", '"moi'))
        self.assertIn("Komento eteen haluaa syötteen tyyppiä", self.captured_output.getvalue())

    def test_missing_quotation_raises_exception(self):
        with self.assertRaises(SystemExit) as error:
            Analyzer(self.create_tree_with_one_command("tulosta", 'moi'))
        self.assertIn("Komento tulosta haluaa syötteen tyyppiä", self.captured_output.getvalue())

    def test_child_is_correct_numeric(self):
        Analyzer(self.create_tree_with_one_command("eteen", '5.5'))
        self.assertNotIn("Komento eteen haluaa syötteen tyyppiä", self.captured_output.getvalue())

    def test_show_works_with_strings(self):
        Analyzer(self.create_tree_with_one_command("tulosta", '"moi'))
        self.assertNotIn("Komento tulosta haluaa syötteen tyyppiä", self.captured_output.getvalue())

    def test_show_works_with_numbers(self):
        Analyzer(self.create_tree_with_one_command("tulosta", '5'))
        self.assertNotIn("Komento tulosta haluaa syötteen tyyppiä", self.captured_output.getvalue())
