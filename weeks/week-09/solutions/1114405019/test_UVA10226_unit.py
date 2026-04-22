import unittest
from io import StringIO
import sys

# Import the solver logic
from UVA10226_handwritten import solve

class TestUVA10226(unittest.TestCase):
    def test_sample_case(self):
        sample_input = "1\n\nRed Alder\nAsh\nAspen\nAsh\nCherries\nMaple\n"
        expected_output = "Ash 33.3333\nAspen 16.6667\nCherries 16.6667\nMaple 16.6667\nRed Alder 16.6667\n"

        # Redirect stdin and stdout
        sys.stdin = StringIO(sample_input)
        sys.stdout = StringIO()

        solve()

        output = sys.stdout.getvalue()
        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
