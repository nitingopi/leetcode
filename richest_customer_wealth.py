class Solution(object):
    def maximumWealth(self, accounts:list[list[int]]):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result:list[int] = []
        for i in range(0,len(accounts)):
            customer_sum = 0
            for j in range(len(accounts[i])):
                customer_sum = customer_sum + accounts[i][j]
            result.append(customer_sum)
        result.sort(reverse=True)    
        return result[0]    

    def maximumWealthForEach(self, accounts:list[list[int]]):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highest_bank_balance = 0
        for customer in accounts:
            customer_wealth = 0
            for bank_balance in customer:
                customer_wealth += bank_balance
            if customer_wealth > highest_bank_balance:
                highest_bank_balance = customer_wealth
        return highest_bank_balance       

    def maximumWealthMagic(self, accounts:list[list[int]]):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """     
        highest_bank_balance:int = 0
        for customer in accounts:
            customer_wealth = sum(customer)
            highest_bank_balance = max(highest_bank_balance,customer_wealth)
        return highest_bank_balance    

solution = Solution()
accounts:list[list[int]] = [[1,2,3],[3,2,1]]
result = solution.maximumWealthMagic(accounts)
print(accounts)
print(result)
accounts:list[list[int]] = [[1,5],[7,3],[3,5]]
result = solution.maximumWealthMagic(accounts)
print(accounts)
print(result)
accounts:list[list[int]] = [[2,8,7],[7,1,3],[1,9,5]]
result = solution.maximumWealthMagic(accounts)
print(accounts)
print(result)