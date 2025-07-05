class Solution(object):
    def findMaxAverage(self, nums:list[int], k:int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0 
        right = k
        current_sum = float(sum(nums[:right]))    
        # print(f"{current_sum=}")
        max_avg = float(current_sum/k)    
        # print(f"{max_avg=}")
        current_window = nums[left:right]
        # print(f"{current_window=}")
        while right < len(nums):
            current_sum = current_sum + nums[right] - nums[left]
            right += 1
            left += 1
            # print(f"{current_window=}")
            # print(f"{max_avg=}")
            max_avg = max(max_avg, float(current_sum/k))
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
