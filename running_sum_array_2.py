class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ret_nums = []
        # ret_nums.insert(0,nums[0])
        for i in range(1,len(nums)):
            # insert will shift the values from original index, and replace with new value
            # nums.insert(i,(nums[i-1]+nums[i]))
            nums[i] = nums[i-1]+nums[i]
        return nums
    
solution = Solution()
nums = [1,2,3,4]
resut = solution.runningSum(nums) 
print(nums)
print(resut)
nums = [1,1,1,1,1]
resut = solution.runningSum(nums) 
print(nums)
print(resut)
nums = [3,1,2,10,1]
resut = solution.runningSum(nums) 
print(nums)
print(resut)   