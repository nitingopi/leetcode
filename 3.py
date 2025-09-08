'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        t:dict = {}
        max_substr = 1
        for i in range(len(s)):
            counter = 1
            t = {s[i]:1}
            for j in range(i+1, len(s)):
                if s[j] in t.keys():
                    break
                else:
                    t[s[j]] = 1
                    counter += 1
            max_substr = max(max_substr,counter)
        return max_substr                   


sol = Solution()
s = "abcabcbb"
ans = sol.lengthOfLongestSubstring(s)        
print(f"{ans=}") # 3
s = "bbbbb"
ans = sol.lengthOfLongestSubstring(s)        
print(f"{ans=}") # 1
s = "pwwkew"
ans = sol.lengthOfLongestSubstring(s)        
print(f"{ans=}") # 3
s = "au"
ans = sol.lengthOfLongestSubstring(s)        
print(f"{ans=}") # 2
s = "dvdf"
ans = sol.lengthOfLongestSubstring(s)        
print(f"{ans=}") # 3