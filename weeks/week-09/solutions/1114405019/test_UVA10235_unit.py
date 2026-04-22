import unittest
from io import StringIO
import sys
from UVA10235_handwritten import solve

class TestUVA10235(unittest.TestCase):
    def test_emirp_cases(self):
        sample_input = "17\n13\n199\n"
        expected_output = "17 is emirp.\n13 is emirp.\n199 is prime.\n"

        sys.stdin = StringIO(sample_input)
        sys.stdout = StringIO()

        solve()

        output = sys.stdout.getvalue()
        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
