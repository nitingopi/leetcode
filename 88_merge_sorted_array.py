class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

    def say_helloworld(self):
        print("hello world")

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
# solution.say_helloworld()
lowest = nums1[0]     
for i in range(0,m-1):
    for j in range(i,n-1):
        if nums1[i]<nums2[j]:
            lowest=nums1[i]
