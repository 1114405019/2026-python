"""
UVA 10235 - Simply Emirp
Technical Adjutant Analysis:
- System Framework: Prime Number Identification and Reversibility Validation.
- Algorithm: Sieve of Eratosthenes for O(1) lookup.
- Complexity:
    - Time: O(M log log M) for pre-computing primes up to M=1,000,000. O(1) per query.
    - Space: O(M) for the boolean prime array.
"""

import sys

def get_is_prime(n):
    """
    Sieve of Eratosthenes to pre-calculate prime numbers.
    Complexity: O(n log log n)
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return is_prime

def solve():
    # Technical constraint: max value in problem is 1,000,000
    primes = get_is_prime(1000000)

    # Read all inputs from stdin
    input_data = sys.stdin.read().split()

    for n_str in input_data:
        n = int(n_str)

        # Primary condition: is n prime?
        if not primes[n]:
            print(f"{n} is not prime.")
        else:
            # Secondary condition: is the reversal of n also prime and not equal to n?
            rev_n_str = n_str[::-1]
            rev_n = int(rev_n_str)

            # Emirp definition: n is prime, reversed n is prime, and n != reversed n
            if n != rev_n and rev_n < 1000000 and primes[rev_n]:
                print(f"{n} is emirp.")
            else:
                print(f"{n} is prime.")

if __name__ == "__main__":
    solve()
