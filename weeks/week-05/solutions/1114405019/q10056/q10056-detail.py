import sys

def solve():
    """
    UVA 10056 - What is the Probability?
    
    Goal: Find the probability that the i-th player wins in a game with N players, 
    where each player has a success probability p in a single throw.
    
    The players throw in order: 1, 2, ..., N, 1, 2, ..., N, ...
    
    The i-th player wins if:
    - They win on their 1st turn: (1-p)^(i-1) * p
    - They win on their 2nd turn: (1-p)^(N + i-1) * p
    - They win on their 3rd turn: (1-p)^(2N + i-1) * p
    - ...
    
    This is an infinite geometric series:
    a = (1-p)^(i-1) * p
    common ratio r = (1-p)^N
    
    Sum S = a / (1 - r) = [ (1-p)^(i-1) * p ] / [ 1 - (1-p)^N ]
    """
    
    # Read input tokens
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    # Number of test cases
    s = int(input_data[idx])
    idx += 1
    
    for _ in range(s):
        # N = number of players, p = success probability, i = target player index
        n = int(input_data[idx])
        p = float(input_data[idx + 1])
        i = int(input_data[idx + 2])
        idx += 3
        
        # If success probability is 0, no one can ever win
        if p == 0:
            print("0.0000")
            continue
            
        # Probability of failure (not winning in a single throw)
        q = 1.0 - p
        
        # Calculate the numerator: probability of winning on the first cycle for player i
        # i-1 people must fail, then player i succeeds
        first_win_prob = (q ** (i - 1)) * p
        
        # Calculate the common ratio: probability that everyone fails in one full cycle
        # All N people fail
        full_cycle_fail_prob = q ** n
        
        # Use geometric series formula: S = a / (1 - r)
        total_prob = first_win_prob / (1.0 - full_cycle_fail_prob)
        
        # Output formatted to 4 decimal places
        print(f"{total_prob:.4f}")

if __name__ == "__main__":
    solve()
