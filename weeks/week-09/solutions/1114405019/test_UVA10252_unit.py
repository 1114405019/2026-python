import unittest
from io import StringIO
import sys
from UVA10252_handwritten import solve

class TestUVA10252(unittest.TestCase):
    def test_common_permutation(self):
        sample_input = "pretty\nwomen\nwalking\ndown\n"
        expected_output = "e\nnw\n"

        sys.stdin = StringIO(sample_input)
        sys.stdout = StringIO()

        solve()

        output = sys.stdout.getvalue()
        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
