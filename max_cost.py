def find_max_cost(arr):
    """
    Finds the maximum possible cost by calculating the max of the squares
    of the maximum and minimum subarray sums.
    """
    if not arr:
        return 0

    # Initialize variables for finding max and min subarray sums
    max_so_far = arr[0]
    min_so_far = arr[0]
    
    current_max = arr[0]
    current_min = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        
        # Calculate max subarray sum ending at current position
        # A new subarray can start at 'num' or extend the previous max subarray
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
        
        # Calculate min subarray sum ending at current position
        # A new subarray can start at 'num' or extend the previous min subarray
        current_min = min(num, current_min + num)
        min_so_far = min(min_so_far, current_min)

    # The max_cost is the square of the maximum absolute sum
    # which is the max of the squares of the max and min sums
    return max(max_so_far**2, min_so_far**2)

# Example usage
arr = [1, 2, 3]
result = find_max_cost(arr)
print(f"For the array {arr}, the max_cost is: {result}")

# Example with negative numbers
arr_neg = [10, -1, 5, -20]
result_neg = find_max_cost(arr_neg)
print(f"For the array {arr_neg}, the max_cost is: {result_neg}")
# The maximum sum is from [10, -1, 5] -> sum=14, square=196
# The minimum sum is from [-20] -> sum=-20, square=400. The max_cost is 400.

arr = [1,-1,1,-1,1]
result = find_max_cost(arr)
print(f"For the array {arr}, the max_cost is: {result}")