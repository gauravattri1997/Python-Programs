t = int(input())
for i in range(0,t):
    r=0
    n,m,c = map(int,input().split())
    n,m = min(n,m),max(n,m)
    for j in range(1,c+1):
        if c%j == 0 :
            if j<=m and (c/j)<=m:
               if j<=n:
                   r += 1
    print (r)
