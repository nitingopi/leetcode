import math
def find_group(n :int) -> int:
    '''
    find all pythagoreas triples where a^2 + b^2 = c^2
    a , b , c from 1 to n
    '''
    '''
    if n = 5
    1,2,3,4,5
    2,3,5 - 9+16=25
    a,b,c -> 1,2,3
    1,2,4 - 1,2,5 
    a<b
    a<b<c
    c<n
    a = i , max=n-2
    b = i+1 max=n-1
    c = i+2 max=n
    while a < n-2:
        while b<n-1:
            while c<n:
                check(a,b,c)
                c++
    result_set = []            
    for a in range(1,n-1):
        for b in range(2,n):
            for c in range(3,n+1):
                if a*a + b*b == c*c:
                   result_set.append((a,b,c)) 

    '''
    result_set = []            
    for a in range(1,n-1):
        for b in range(a+1,n):
            for c in range(b+1,n+1):
                if a*a + b*b == c*c:
                   result_set.append((a,b,c))
    return result_set
n = 5
ans = find_group(n)
print(f"{ans=}")

n = 10
ans = find_group(n)
print(f"{ans=}")
            
                
    
    