class Solution(object):

    def number_of_steps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num & 1 == 0:
                num >>= 1
            else:
                num -= 1
            steps += 1        
        
        return steps


solution = Solution()
num:int = 14
steps = solution.number_of_steps(num)
print(f"{steps=}")
num:int = 8
steps = solution.number_of_steps(num)
print(f"{steps=}")
num:int = 123
steps = solution.number_of_steps(num)
num:int = 3
steps = solution.number_of_steps(num)
print(f"{steps=}")