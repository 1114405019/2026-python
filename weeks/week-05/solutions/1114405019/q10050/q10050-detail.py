import sys

def solve():
    """
    Hartals problem (UVA 10050)
    We need to count how many work days are lost due to strikes (hartals).
    N: Total days to simulate.
    P: Number of political parties.
    h_i: Hartal parameter for party i.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    # Number of test cases
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        # Total number of days in the simulation
        n = int(input_data[idx])
        idx += 1
        
        # Number of political parties
        p = int(input_data[idx])
        idx += 1
        
        # Store the hartal parameters for each party
        hartal_params = []
        for _ in range(p):
            hartal_params.append(int(input_data[idx]))
            idx += 1
            
        lost_days_count = 0
        
        # Loop through each day from 1 to N
        for day in range(1, n + 1):
            # Check if it's a weekend (Friday or Saturday)
            # Week starts on Sunday (day 1).
            # Sunday=1, Monday=2, Tuesday=3, Wednesday=4, Thursday=5, Friday=6, Saturday=7(0)
            if day % 7 == 6 or day % 7 == 0:
                # It's a holiday, skip checking strikes
                continue
            
            # Check if any party has a hartal on this day
            is_hartal_day = False
            for h in hartal_params:
                if day % h == 0:
                    is_hartal_day = True
                    break
            
            # If at least one party has a hartal, it's a lost working day
            if is_hartal_day:
                lost_days_count += 1
                
        # Output the total number of lost days for the current case
        print(lost_days_count)

if __name__ == "__main__":
    solve()
