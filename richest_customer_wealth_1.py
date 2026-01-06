class Solution(object):
    def maximumWealth(self, accounts:list[list[int]]):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest=0
        for account in accounts:
            # wealth=0
            # for money in account:
            #     wealth += money
            wealth = sum(account)    
            richest=max(richest,wealth)    
        return richest
    
solution = Solution()
accounts:list[list[int]] = [[1,2,3],[3,2,1]]
result = solution.maximumWealth(accounts)
print(accounts)
print(result)
accounts:list[list[int]] = [[1,5],[7,3],[3,5]]
result = solution.maximumWealth(accounts)
print(accounts)
print(result)
accounts:list[list[int]] = [[2,8,7],[7,1,3],[1,9,5]]
result = solution.maximumWealth(accounts)
print(accounts)
print(result)