import unittest
import sys, io
from compile import openfile

class testCompile(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO() 
        sys.stdout = self.capturedOutput

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_no_file_provided(self):
        openfile([])
        self.assertIn("Et antanut tiedostoa käännettäväksi.", self.capturedOutput.getvalue())

    def test_too_many_files_provided(self):
        openfile(["file1", "file2"])
        self.assertIn("Annoit liian monta tiedostoa käännettäväksi.", self.capturedOutput.getvalue())


