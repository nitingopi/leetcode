'''
Problem Description:

Given an array nums, you are asked to return a new array runningSum where runningSum[i] is the running sum of nums.

The running sum is defined as runningSum[i] = nums[0] + nums[1] + ... + nums[i].

In simpler terms: For each element in the original array, you need to calculate the sum of all elements up to and including that element, and store it in a new array.

Input:

nums: A 1D integer array (list in Python).

Output:

runningSum: A new 1D integer array of the same size, containing the running sum.

Example 1:

Input: nums = [1, 2, 3, 4]

Output: [1, 3, 6, 10]

Explanation:

runningSum[0] = 1

runningSum[1] = 1 + 2 = 3

runningSum[2] = 1 + 2 + 3 = 6

runningSum[3] = 1 + 2 + 3 + 4 = 10
'''

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret_nums = []
        for i in range(1,len(nums)+1):
            print(f"{i=}")
            sum = 0
            for j in range(0,i):
                print(f"{j=}")
                sum = sum+nums[j]
            ret_nums.append(sum)
        return ret_nums
    
solution = Solution()
# nums = [1,2,3,4]
# nums = [1,1,1,1,1]
nums = [3,1,2,10,1]
resut = solution.runningSum(nums) 
print(nums)
print(resut)   