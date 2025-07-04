def diffuse_bomb(code:list[int],k:int):
    n = len(code)
    new_code = []
    if k == 0 :
        for i in range(len(code)):
            code[i] = 0
        return code
    for i in range(n):
        current_sum = 0
        for j in range(1,abs(k)+1):
            if k > 0:
                current_sum += code[(i+j)%n]
            else:
                current_sum += code[(i-j+n)%n]
        new_code.append(current_sum)
    return new_code


code = [5, 7, 1, 4]
k = 3
ans = diffuse_bomb(code, k)
print(f"{ans=}")
code = [5, 7, 1, 4]
k = 0
ans = diffuse_bomb(code, k)
print(f"{ans=}")
code = [2, 4, 9, 3]
k = -2
ans = diffuse_bomb(code, k)
print(f"{ans=}")
