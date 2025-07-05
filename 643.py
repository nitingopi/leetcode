class Solution(object):
    def findMaxAverage(self, nums:list[int], k:int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = sum(nums[:k])    
        max_avg = current_sum/k    
        for i in range(len(nums)-k+1):
            current_sum = sum(nums[i:i+k])
            max_avg = max(max_avg,current_sum/k)    
        return max_avg


solutionobj = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
ans = solutionobj.findMaxAverage(nums, k)   # 12.75000     
print(f"{ans=}")
nums = [5]
k = 1
ans = solutionobj.findMaxAverage(nums, k)   #  5.00000     
print(f"{ans=}")
nums = [-1]
k = 1
ans = solutionobj.findMaxAverage(nums, k)   # -1.00000     
print(f"{ans=}")
