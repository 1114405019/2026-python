import sys

# Geometric series simulation (approximate)
# Instead of the formula, we can simulate cycles until probability is negligible.
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    s_cases = int(input_data[idx])
    idx += 1
    
    for _ in range(s_cases):
        n = int(input_data[idx])
        p = float(input_data[idx + 1])
        i = int(input_data[idx + 2])
        idx += 3
        
        if p == 0:
            print("0.0000")
            continue
            
        q = 1.0 - p
        total_prob = 0
        current_fail_prob = 1.0
        
        # Simulate many cycles to get enough precision
        # (q^n)^k becomes very small quickly unless p is extremely small
        for cycle in range(10000):
            # Probability player i wins in this cycle
            # (failure for all previous cycles) * (failure for players before i in this cycle) * success
            win_this_turn = (current_fail_prob) * (q ** (i - 1)) * p
            total_prob += win_this_turn
            
            # Probability everyone fails this cycle
            current_fail_prob *= (q ** n)
            
            # If addition is too small to matter, stop
            if win_this_turn < 1e-12:
                break
                
        print(f"{total_prob:.4f}")

if __name__ == "__main__":
    solve()
