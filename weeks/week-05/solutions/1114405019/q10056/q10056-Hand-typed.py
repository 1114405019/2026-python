import sys

def main():
    # A slightly more 'manual' looking version
    input_str = sys.stdin.read()
    tokens = input_str.split()
    
    if not tokens:
        return
        
    case_count = int(tokens[0])
    curr = 1
    
    for _ in range(case_count):
        n = int(tokens[curr])
        p = float(tokens[curr+1])
        i = int(tokens[curr+2])
        curr += 3
        
        if p < 1e-9:
            print("0.0000")
            continue
            
        q = 1.0 - p
        # probability = p * q^(i-1) / (1 - q^n)
        res = (p * (q ** (i - 1))) / (1 - (q ** n))
        
        # Rounding to 4 decimal places
        print("{:.4f}".format(res))

if __name__ == "__main__":
    main()
