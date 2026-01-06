'''
Docstring for 1_two_sum_bruteforce
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

'''
bruteforece

def two_sum(nums,target):
    for i in range(len(nums)):
        cand_1 = nums[i]
        cand_2 = target-cand_1
        for j in range(i+1,len(nums)):
            if nums[j] == cand_2:
                return [i,j]       
'''

def two_sum(nums, target):
    '''
    [2,7,11,15], 9
    map_candidates = { 2:0,  }
    9-7=2
    '''
    map_candidates = {}
    for i in range(len(nums)):
        if nums[i] in map_candidates.keys():
            return (map_candidates[nums[i]],i)
        map_candidates[target-nums[i]]=i




nums = [2, 7, 11, 15]
target = 9
ans = two_sum(nums,target)
print(f"{ans=}")
nums = [3, 2, 4]
target = 6
ans = two_sum(nums,target)
print(f"{ans=}")
nums = [3, 3]
target = 6
ans = two_sum(nums,target)
print(f"{ans=}")
