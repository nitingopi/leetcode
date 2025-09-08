def diffuse_bomb(code:list[int],k:int):
    n = len(code)
    new_code = [0]*n
    if k == 0:
        return new_code
    current_index = 0
    if k > 0:
        start = current_index+1
        end = current_index+k
        new_code[0] = window_sum = sum(code[start:k+1])
    if k < 0:
        start = (current_index-k+n)%n
        end = (current_index-1+n)%n
        new_code[0] = window_sum = sum(code[start:end+1])
    for i in range(1,n):
        new_code[i] = window_sum = window_sum - code[start] + code[(end+1)%n]
        start = (start+1)%n 
        end = (end+1)%n
    return new_code    

code = [5, 7, 1, 4]
k = 3
ans = diffuse_bomb(code, k) # [12,10,16,13]
print(f"{ans=}")
code = [5, 7, 1, 4]
k = 0
ans = diffuse_bomb(code, k) # [0,0,0,0]
print(f"{ans=}")
code = [2, 4, 9, 3] # [12,5,6,13]
k = -2
ans = diffuse_bomb(code, k)
print(f"{ans=}")
