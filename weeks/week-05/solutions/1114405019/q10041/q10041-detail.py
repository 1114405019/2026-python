import sys

def solve():
    """
    Vito's Family problem (UVA 10041)
    Goal: Find a house location that minimizes the total distance to all relatives.
    The optimal location is the median of the coordinates.
    """
    
    # Read the entire input from standard input and split into tokens
    input_data = sys.stdin.read().split()
    
    # If there is no input, we just return
    if not input_data:
        return
    
    # Keep track of the current position in the input list
    current_index = 0
    
    # The first number is the number of test cases (T)
    test_cases_count = int(input_data[current_index])
    current_index += 1
    
    # Process each test case
    for _ in range(test_cases_count):
        # The first number in each test case is the number of relatives (r)
        relatives_count = int(input_data[current_index])
        current_index += 1
        
        # Collect the house numbers of all relatives
        house_numbers = []
        for i in range(relatives_count):
            house_numbers.append(int(input_data[current_index]))
            current_index += 1
            
        # Sort the house numbers to find the median.
        # Sorting is necessary because the median minimizes the sum of absolute differences.
        house_numbers.sort()
        
        # Find the median element. 
        # For an odd number of elements, it's the middle one.
        # For an even number of elements, any value between the two middle ones works.
        # Using the index relatives_count // 2 works for both.
        optimal_location = house_numbers[relatives_count // 2]
        
        # Calculate the sum of distances from the optimal location to each relative's house
        total_distance = 0
        for house in house_numbers:
            # abs() function computes the absolute value |house - optimal_location|
            total_distance += abs(house - optimal_location)
            
        # Print the result for the current test case
        print(total_distance)

if __name__ == "__main__":
    # Start the program execution
    solve()
