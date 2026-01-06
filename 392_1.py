'''
Given two strings, $s$ and $t$, return true if $s$ is a subsequence of $t$, 
or false otherwise.A subsequence of a string is a new string that can be 
formed from the original string by deleting some (or none) of the 
characters without disturbing the relative order of the remaining characters.
'''

def is_subsequence(t:str, s:str) -> bool:
    # solve using 2 pointer method
    p1:int=0 # pointer in s
    p2:int=0 # pointer in t
    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1
    if p1 == len(s):
        return True
    return False

s:str = "abc"
t:str = "ahbgdc"
ans = is_subsequence(t,s)
print(ans)
s = "axc"
t = "ahbgdc"
ans = is_subsequence(t,s)
print(ans)
s = ""
t = "abc"
ans = is_subsequence(t,s)
print(ans)
s = "ace"
t = "abcde"
ans = is_subsequence(t,s)
print(ans)
