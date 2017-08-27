t = int(input())
for i in range(0,t):
    n = int(input())
    p = list(map(int,input().split()))
    g = []
    for j in range(0,n-1):
        g.append(list(map(int,input().split())))
    for j in range(0,n):
        q = p.copy()
        q[j] = 0
        for k in range(0,n-1):
            if g[k][0]==j+1:
                q[g[k][1]-1] = 0
            elif g[k][1]==j+1:
                q[g[k][0]-1] = 0
        if q.count(0)==n:
            print("0",end=' ')
        else :
            print(q.index(max(q))+1,end=' ')
