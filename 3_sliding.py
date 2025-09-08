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
        l = r = 0
        char_map = {}
        max_str = 0
        while r < len(s):
            if s[r] in char_map.keys():
                if char_map[s[r]] >= l:
                    l = char_map[s[r]]+1
            char_map[s[r]] = r
            max_str = max(max_str, r-l+1)
            r += 1
        return max_str    



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