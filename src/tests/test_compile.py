import unittest
import sys, io
from unittest.mock import MagicMock, PropertyMock
from compile import openfile
import src.error_handler

class testCompile(unittest.TestCase):

    def test_no_file_provided(self):
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput
        openfile([])
        sys.stdout = sys.__stdout__
        self.assertIn("Et antanut tiedostoa käännettäväksi.", capturedOutput.getvalue())

    
    def test_too_many_files_provided(self):
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput
        openfile(["file1", "file2"])
        sys.stdout = sys.__stdout__
        self.assertIn("Annoit liian monta tiedostoa käännettäväksi.", capturedOutput.getvalue())


