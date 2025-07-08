def is_subsequence(t:str, s:str) -> bool:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len(s):
        return True
    else:
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
