from decimal import *

t = int(input())
for i in range(0,t):
    u,v = map(int,input().split())
    a = Decimal((u+v)*(u+v+1))/Decimal(2)
    r = int(a)+u+1
    print(r)
