import unittest
from io import StringIO
import sys
from UVA10268_handwritten import solve

class TestUVA10268(unittest.TestCase):
    def test_derivative(self):
        sample_input = "7\n1 -1\n2\n1 1 1\n"
        expected_output = "1\n5\n"

        sys.stdin = StringIO(sample_input)
        sys.stdout = StringIO()

        solve()

        output = sys.stdout.getvalue()
        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
