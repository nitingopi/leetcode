class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer:list[str] = []
        for i in range(1,n+1):
            divisible_by_3:bool = i%3 == 0
            divisible_by_5:bool = i%5 == 0
            current_str:str = ""
            if divisible_by_3:
                current_str += "Fizz"
            if divisible_by_5:
                current_str += "Buzz"     
            if current_str == "":
                current_str = str(i) 
            answer.append(current_str)       
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
