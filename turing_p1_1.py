def find_group(n :int) -> int:
    '''
    find all pythagoreas triples where a^2 + b^2 = c^2
    a , b , c from 1 to n
    '''
    triplets= set()
    if n < 3 :
        return triplets
    '''
    n = 3
    3 pointers
    p1 -> i
    p2 -> i+1
    p3 -> i+2
    keep moving p3 -> right side until p3 = n
    then start moving p2 -> right side until p2 = n-1
    then start moving p3 -> right side until p3 = n-2

    lets say n=5
    p1=1, p2=2, p3=3
    p1=1,  p3=4
    p3=5
    p2=3
    p2=4
    p1=2
    p1=3

    '''
    p1:int = 1
    p2:int = p1+1
    p3:int = p2+1
    while p1 <= n-2:
        if p3*p3 == p2*p2 + p1*p1:
            triplets.add((p1,p2,p3))
        if p3 < n:
            p3 += 1    
        elif p3 == n and p2 < n-1:
            p2 += 1
        elif p3 == n and p2 == n-1:
            p1 += 1
    return triplets                


n = 5
# ans = find_group(n)
# print(f"{ans=}")

n = 10
ans = find_group(n)
print(f"{ans=}")
            
                
    
    