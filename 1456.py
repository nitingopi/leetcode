class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a','e','i','o','u'}
        left = 0
        right = k
        count_vowels = max_vowels = 0 
        for i in range(k):
            if s[i] in vowels:
                count_vowels += 1        
        max_vowels = count_vowels
        while right < len(s):       # 8 < 9 
            if s[left] in vowels:
                count_vowels -= 1
            if s[right] in vowels:
                count_vowels += 1
            max_vowels = max(max_vowels,count_vowels)                
            left += 1
            right += 1
        return max_vowels
    
solution_obj = Solution()
s:str = "abciiidef"
k:int = 3
ans = solution_obj.maxVowels(s,k)
print(f"{ans=}")

s = "aeiou"
k = 2
ans = solution_obj.maxVowels(s,k)
print(f"{ans=}")

s = "leetcode"
k = 3
ans = solution_obj.maxVowels(s,k)
print(f"{ans=}")
