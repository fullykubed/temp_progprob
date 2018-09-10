import unittest
from io import StringIO
import sys

from diamond import printDiamond, START_CHAR, OUTER_SPACER, INNER_SPACER

class TestPrintDiamond(unittest.TestCase):

    #redirect standard out to a string buffer for testing
    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
    def tearDown(self):
        del self._stringio
        sys.stdout = self._stdout

    #tests
    def test_invalid(self):
        with self.assertRaises(ValueError) as context:
            printDiamond("1")
        self.assertTrue("Ending character must be an alphabetic character" in str(context.exception))

    def test_startOnly(self):
        printDiamond(START_CHAR)
        self.assertEqual(self._stringio.getvalue(), START_CHAR + "\n")

    def test_upToZ(self):
        with open("upToZ.txt", "r") as file:
            printDiamond("Z")
            expected = file.read()
            actual = self._stringio.getvalue().replace(OUTER_SPACER, " ").replace(INNER_SPACER, " ")
            self.assertEqual(actual, expected)

    def test_upToG(self):
        with open("upToG.txt", "r") as file:
            printDiamond("G")
            expected = file.read()
            actual = self._stringio.getvalue().replace(OUTER_SPACER, " ").replace(INNER_SPACER, " ")
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()