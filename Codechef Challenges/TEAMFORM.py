t=int(input())
for i in range(0,t):
    n,m = map(int,input().split())
    u,v =[],[]
    for j in range(0,m):
        t1,t2 = map(int,input().split())
        u.append(t1)
        v.append(t2)
    if n%2 is 0:
        print('yes')
    else:
        print('no')
