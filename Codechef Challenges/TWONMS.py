t=int(input())
for i in range(t):
    a,b,n = map(int,input().split())
    if n%2 is 1:
        a *= 2
    p = max(a,b)/min(a,b)
    print(int(p))
