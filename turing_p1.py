import math
def find_group(n :int) -> int:
    '''
    find all pythagoreas triples where a^2 + b^2 = c^2
    a , b , c from 1 to n
    '''
    ans = 0
    tripets = set()
    for a in range(1,n-1):
        for b in range(a+1,n):
            c_squared = a**2 + b**2
            c = math.sqrt(c_squared)
            if c == int(c) and c <= n:
                ans += 1
                tripets.add((a,b,int(c)))
    print(tripets)
    return ans



n = 5
ans = find_group(n)
print(f"{ans=}")

n = 10
ans = find_group(n)
print(f"{ans=}")
            
                
    
    