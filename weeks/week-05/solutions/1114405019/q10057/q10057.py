import sys

def solve():
    # Read all input. Multi-line, multiple test cases.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        try:
            n = int(input_data[idx])
            idx += 1
            nums = []
            for _ in range(n):
                nums.append(int(input_data[idx]))
                idx += 1
            
            nums.sort()
            
            if n % 2 == 1:
                mid1 = nums[n // 2]
                smallest_a = mid1
                # Count occurrences of mid1 in input
                count_in_input = 0
                for x in nums:
                    if x == mid1:
                        count_in_input += 1
                possible_a_count = 1
            else:
                mid1 = nums[n // 2 - 1]
                mid2 = nums[n // 2]
                smallest_a = mid1
                # Count numbers in range [mid1, mid2]
                count_in_input = 0
                for x in nums:
                    if x >= mid1 and x <= mid2:
                        count_in_input += 1
                possible_a_count = mid2 - mid1 + 1
            
            print(f"{smallest_a} {count_in_input} {possible_a_count}")
        except (ValueError, IndexError):
            break

if __name__ == "__main__":
    solve()
