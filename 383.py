'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 
'''

class Solution(object):
    def canConstruct(self, ransomNote:str, magazine:str):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = {}
        for i in magazine:
            value =  mag_dict.get(i,0)
            mag_dict[i] = value + 1
        for j in ransomNote:
            if j not in mag_dict.keys():
                return False
            if mag_dict.get(j) == 0:
                return False    
            mag_dict[j] = mag_dict[j] - 1
        return True

solution_obj = Solution()
ransomNote:str = "aa"
magazine:str = "aab"
ans:bool = solution_obj.canConstruct(ransomNote, magazine)
print(f"{ans=}")    




