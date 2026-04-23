import sys

def solve():
    """
    UVA 10057 - A Mid-summer Night's Dream
    Goal: Find an integer A that minimizes the sum of absolute differences to a set of numbers.
    The value(s) of A that minimize sum|Xi - A| are the median(s).
    
    Output requirements:
    1. The smallest such integer A.
    2. The number of Xi in the input that can be a value of A to minimize the formula.
       (This actually means how many elements from the input are in the range [min_median, max_median])
    3. The total number of possible integer values for A that minimize the formula.
    """
    
    # Read all input data and split into a list of strings
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        try:
            # Number of integers in this test case
            n = int(input_data[idx])
            idx += 1
            
            # The list of numbers
            nums = []
            for _ in range(n):
                nums.append(int(input_data[idx]))
                idx += 1
            
            # Sort the numbers to find the median
            nums.sort()
            
            # Case 1: Odd number of elements
            if n % 2 == 1:
                # The median is the single middle element
                median1 = nums[n // 2]
                
                # Smallest A is just the median
                smallest_a = median1
                
                # Count how many of the input numbers are equal to this median
                count_in_input = 0
                for x in nums:
                    if x == median1:
                        count_in_input += 1
                
                # Only one integer (the median itself) minimizes the sum
                possible_a_count = 1
                
            # Case 2: Even number of elements
            else:
                # Any integer between the two middle elements (inclusive) minimizes the sum
                median1 = nums[n // 2 - 1] # Lower median
                median2 = nums[n // 2]     # Upper median
                
                # Smallest A is the lower median
                smallest_a = median1
                
                # Count how many of the input numbers are between median1 and median2 (inclusive)
                count_in_input = 0
                for x in nums:
                    if x >= median1 and x <= median2:
                        count_in_input += 1
                
                # The number of integers in the range [median1, median2] is (median2 - median1 + 1)
                possible_a_count = median2 - median1 + 1
            
            # Print the result for the current test case
            print(f"{smallest_a} {count_in_input} {possible_a_count}")
            
        except (ValueError, IndexError):
            # End of input reached
            break

if __name__ == "__main__":
    solve()
