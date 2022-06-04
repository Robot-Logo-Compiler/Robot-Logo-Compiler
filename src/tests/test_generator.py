import unittest

class TempTest(unittest.TestCase): # Tämä testiluokka on väliaikainen ja on tarkoitus korvata testeillä koodigeneraattorille
    def test_does_testing_work(self):
        self.assertEqual(1,1)