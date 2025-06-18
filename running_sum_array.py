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