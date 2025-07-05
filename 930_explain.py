"""
UNDERSTANDING: right - left + 1

The key question: Given a valid window from index 'left' to 'right', 
how many subarrays END at position 'right'?

Let's visualize this step by step:
"""

def explain_right_minus_left_plus_one():
    """
    Visual explanation of why we add (right - left + 1) at each step
    """
    print("=== UNDERSTANDING right - left + 1 ===\n")
    
    # Example array
    nums = [1, 0, 1, 0, 1]
    print(f"Array: {nums}")
    print("Indices: 0  1  2  3  4\n")
    
    print("Question: At each position 'right', how many subarrays END at that position?\n")
    
    # Let's say we have a valid window from left=1 to right=3
    left, right = 1, 3
    print(f"Example: left={left}, right={right}")
    print(f"Valid window: nums[{left}:{right+1}] = {nums[left:right+1]}")
    print(f"Window indices: {list(range(left, right+1))}")
    print()
    
    print("All subarrays that END at position right=3:")
    
    # Method 1: List all subarrays ending at 'right'
    subarrays_ending_at_right = []
    for start in range(left, right + 1):
        subarray = nums[start:right + 1]
        subarrays_ending_at_right.append((start, right, subarray))
        print(f"  Start at {start}, end at {right}: {subarray}")
    
    count_method1 = len(subarrays_ending_at_right)
    print(f"\nTotal subarrays ending at right={right}: {count_method1}")
    
    # Method 2: Calculate using formula
    count_method2 = right - left + 1
    print(f"Using formula (right - left + 1): {right} - {left} + 1 = {count_method2}")
    
    print(f"Both methods give same result: {count_method1 == count_method2}")
    print()
    
    print("=== WHY THE FORMULA WORKS ===")
    print("Starting positions for subarrays ending at 'right':")
    positions = list(range(left, right + 1))
    print(f"Possible starting positions: {positions}")
    print(f"Number of positions: {len(positions)}")
    print(f"This equals: (last_position - first_position + 1) = ({right} - {left} + 1) = {count_method2}")


def demonstrate_with_concrete_example():
    """
    Concrete example showing the counting at each step
    """
    print("\n" + "="*50)
    print("CONCRETE EXAMPLE: nums = [1, 0, 1], target = 2")
    print("="*50)
    
    nums = [1, 0, 1]
    target = 2
    
    left = 0
    current_sum = 0
    total_count = 0
    
    print("Step by step execution:")
    print()
    
    for right in range(len(nums)):
        current_sum += nums[right]
        print(f"Step {right + 1}: right = {right}, nums[{right}] = {nums[right]}")
        print(f"  current_sum = {current_sum}")
        
        # Shrink window if needed
        while current_sum > target:
            print(f"  Sum {current_sum} > target {target}, shrinking...")
            current_sum -= nums[left]
            left += 1
            print(f"  New: left = {left}, current_sum = {current_sum}")
        
        # Count subarrays ending at 'right'
        print(f"  Final window: left = {left}, right = {right}")
        print(f"  Window content: {nums[left:right+1]}")
        print(f"  Subarrays ending at position {right}:")
        
        subarrays_at_this_step = []
        for start in range(left, right + 1):
            subarray = nums[start:right + 1]
            subarray_sum = sum(subarray)
            subarrays_at_this_step.append(subarray)
            print(f"    nums[{start}:{right+1}] = {subarray}, sum = {subarray_sum}")
        
        step_count = right - left + 1
        total_count += step_count
        
        print(f"  Count this step: {step_count}")
        print(f"  Running total: {total_count}")
        print()
    
    print(f"Final result: {total_count} subarrays with sum <= {target}")


def why_plus_one():
    """
    Explain why we need the +1 in the formula
    """
    print("\n" + "="*40)
    print("WHY DO WE ADD +1?")
    print("="*40)
    
    print("Consider positions from left=2 to right=5:")
    print("Positions: 2, 3, 4, 5")
    print()
    
    print("Method 1 - Count directly:")
    positions = [2, 3, 4, 5]
    print(f"Positions: {positions}")
    print(f"Count: {len(positions)}")
    print()
    
    print("Method 2 - Using subtraction:")
    print("right - left = 5 - 2 = 3")
    print("But we have 4 positions, not 3!")
    print()
    
    print("Method 3 - Correct formula:")
    print("right - left + 1 = 5 - 2 + 1 = 4 ✓")
    print()
    
    print("The +1 accounts for inclusive counting:")
    print("- Positions 2,3,4,5 span a range of (5-2) = 3")
    print("- But include both endpoints: 3 + 1 = 4 positions")
    print("- Think: 'How many integers from 2 to 5 inclusive?' → 4")


if __name__ == "__main__":
    explain_right_minus_left_plus_one()
    demonstrate_with_concrete_example()
    why_plus_one()