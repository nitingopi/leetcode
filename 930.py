class Solution(object):
    def numSubarraysWithSum(self, nums:list[int], goal:int):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        counter:int = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum = sum + nums[j]
                if sum == goal:
                    counter += 1
        return counter


solution_obj = Solution()
nums:list[int] = [1,0,1,0,1]
goal:int = 2
ans = solution_obj.numSubarraysWithSum(nums, goal)
print(f"{ans=}")