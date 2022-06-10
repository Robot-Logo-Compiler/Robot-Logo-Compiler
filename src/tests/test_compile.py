import unittest
import sys
from unittest.mock import MagicMock, PropertyMock
from compile import openfile
from src.error_handler import FileNumberException

class testCompile(unittest.TestCase):

    def test_no_file_provided(self):
        sys.argv = ['compile.py']
        with self.assertRaises(FileNumberException):
            openfile()

    
    def test_too_many_files_provided(self):
        pass

