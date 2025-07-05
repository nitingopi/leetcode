class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        current_val = num
        steps = 0
        for i in range(0,num):
            if current_val == 0:
                return steps
            elif current_val%2 == 0:
                current_val = current_val/2
                steps += 1
            else:
                current_val = current_val-1
                steps += 1
        return steps

    def number_of_steps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num%2 == 0:
                num /= 2
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