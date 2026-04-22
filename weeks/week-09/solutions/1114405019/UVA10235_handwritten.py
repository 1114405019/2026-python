import sys

def get_is_prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return is_prime

def solve():
    primes = get_is_prime(1000000)
    input_data = sys.stdin.read().split()
    for n_str in input_data:
        n = int(n_str)
        if not primes[n]:
            print(f"{n} is not prime.")
        else:
            rev_n = int(n_str[::-1])
            if n != rev_n and rev_n < 1000000 and primes[rev_n]:
                print(f"{n} is emirp.")
            else:
                print(f"{n} is prime.")

if __name__ == "__main__":
    solve()
