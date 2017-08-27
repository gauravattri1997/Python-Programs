import math

def pri(t):
    i = 2
    p = int(math.sqrt(t))
    while i<p+1:
        if t%i is 0:
            return False
        i += 1
    return True

n = int(input())
a = list(map(int,input().split()))
q = int(input())
for z in range(0,q):
    l,r,x,y = map(int,input().split())
    result = 0
    if x is 2:
        if y is 2:
            b = [2]
        else:
            b = [2]+list(range(x+1,y+1,2))
    elif x%2 is 0:
        b = list(range(x+1,y+1,2))
    else:
        b = list(range(x,y+1,2))
    for i in b:
        if pri(i):
            for j in a[l-1:r]:
                exponent = 0
                while j%i is 0:
                    exponent += 1
                    j = j//i
                result += exponent
    print(result)
