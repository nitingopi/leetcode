class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer:list[str] = []
        for i in range(1,n+1):
            if i%5 == 0 and i%3 == 0:
                answer.append("FizzBuzz")
            elif i%3 == 0:
                answer.append("Fizz")
            elif i%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
solution = Solution()
n=3
answer = solution.fizzBuzz(n)
print(f"{n=} {answer=}")

n=5
answer = solution.fizzBuzz(n)
print(f"{n=} {answer=}")

n=15
answer = solution.fizzBuzz(n)
print(f"{n=} {answer=}")
