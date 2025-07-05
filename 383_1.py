class Solution(object):
    def canConstruct(self, ransomNote:str, magazine:str):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote:
            index = magazine.find(char)
            if index == -1:
                return False
            magazine = magazine[:index]+magazine[index+1:]
        return True    

solution_obj = Solution()
ransomNote:str = "aa"
magazine:str = "aba"
ans:bool = solution_obj.canConstruct(ransomNote, magazine)
print(f"{ans=}")    




