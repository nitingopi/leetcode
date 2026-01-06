class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # create pointer p1 to point to last element in nums1
        p1 = m-1
        # create pointer p2 to point to last element in nums2
        p2 = n-1
        # create pointer p to point to last element in nums1
        p = m+n-1
        # now loop while p2 >= 0
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            elif p1 >= 0 and nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        return nums1           


    def say_helloworld(self):
        print("hello world")

solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(nums1)
print(nums2)
sorted_array = solution.merge(nums1,m,nums2,n)
print(sorted_array)

nums1 = [1,2,3,6,0,0,0]
m = 4
nums2 = [2,5,6]
n = 3
print(nums1)
print(nums2)
sorted_array = solution.merge(nums1,m,nums2,n)
print(sorted_array)

