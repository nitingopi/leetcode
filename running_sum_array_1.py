class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret_nums = []
        ret_nums.append(nums[0])
        for i in range(1,len(nums)):
            ret_nums.append(ret_nums[i-1]+nums[i])
        return ret_nums
    
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