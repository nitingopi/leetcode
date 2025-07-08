def is_subsequence(t:str, s:str) -> bool:
    prev_index = -1
    for char in  s:
        cur_index = t.find(char)
        if cur_index < prev_index:
            return False
        prev_index = cur_index
        print(f"{cur_index=}")
    return True


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
