import unittest
from io import StringIO
import sys
from UVA10242_handwritten import solve

class TestUVA10242(unittest.TestCase):
    def test_parallelogram_points(self):
        # Sample input with two parallelograms
        sample_input = "0.000 0.000 0.000 1.000 0.000 1.000 1.000 1.000\n1.000 0.000 3.500 3.500 3.500 3.500 0.000 1.000\n"
        expected_output = "1.000 0.000\n-2.500 -2.500\n"

        sys.stdin = StringIO(sample_input)
        sys.stdout = StringIO()

        solve()

        output = sys.stdout.getvalue()
        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
