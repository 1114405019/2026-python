"""
UVA 10268 - 498-bis
Technical Adjutant Analysis:
- System Framework: Polynomial Derivative Evaluator.
- Algorithm: Horner's Method for Derivative Evaluation.
- Complexity:
    - Time: O(n) per test case, where n is the degree of the polynomial.
    - Space: O(n) to store coefficients.
"""

import sys

def solve():
    # Read all lines from standard input
    lines = sys.stdin.read().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        try:
            # x is the value at which the derivative is evaluated
            x = int(line)
            # coeffs are the coefficients of the polynomial P(x) = a_n*x^n + ... + a_1*x + a_0
            coeffs = list(map(int, lines[i+1].split()))
            i += 2
        except (ValueError, IndexError):
            break

        # P(x) = a_n*x^n + a_{n-1}*x^{n-1} + ... + a_1*x + a_0
        # P'(x) = n*a_n*x^{n-1} + (n-1)*a_{n-1}*x^{n-2} + ... + a_1

        n = len(coeffs) - 1
        res = 0

        # Applying Horner's method to evaluate the derivative efficiently.
        # This avoids O(n^2) by not calculating powers of x explicitly.
        # P'(x) = ( ... ((n * a_n) * x + (n-1) * a_{n-1}) * x + ... + 1 * a_1 )
        for j in range(n):
            # j-th coefficient from the left is a_{n-j}.
            # Its power in P(x) is (n-j).
            # Its term in P'(x) is (n-j) * a_{n-j} * x^{n-j-1}.
            res = res * x + coeffs[j] * (n - j)

        # Output the evaluated derivative value
        print(int(res))

if __name__ == "__main__":
    solve()
