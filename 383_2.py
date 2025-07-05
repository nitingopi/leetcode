class Solution(object):
    def canConstruct(self, ransomNote:str, magazine:str):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = list(set(ransomNote))
        if len(ransomNote) > len(magazine):
            return False
        return True
            

solution_obj = Solution()
ransomNote:str = "aa"
magazine:str = "aba"
ans:bool = solution_obj.canConstruct(ransomNote, magazine)
print(f"{ans=}")    




