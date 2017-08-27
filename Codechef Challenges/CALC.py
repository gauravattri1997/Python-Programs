import math

t=int(input())
for zoo in range(t):
    n,b=map(int,input().split())
    x = (n/2)/b
    p,q = math.ceil(x),math.floor(x)
    p,q = (n-b*p)*p,(n-b*q)*q
    print(max(p,q))
