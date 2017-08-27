import math
t = int(input())
for i in range(0,t):
    n,k = map(int,input().split())
    a,dis,qw,la = [0 for w in range(0,k)],0.0,0.0,n
    x,y,s = [],[],[]
    for j in range(0,n):
        xt,yt = map(int,input().split())
        x.append(xt)
        y.append(yt)
    x.append(0)
    y.append(0)
    for j in range(0,n):
        s.append(input())
        for z in range(0,k):
            if s[j][z] is '1':
                a[z] = 1
    if a.count(1) is not k:
        print(-1)
    else:
        while a.count(2) is not k:
            ma = 0
            pos = []
            for w in range(0,n):
                can = 0
                for z in range(0,k):
                    if a[z] is 1 and s[w][z] is '0':
                        can += 1
                if ma<can:
                    pos.clear()
                    pos.append(w)
                    ma = can
                elif ma is can:
                    pos.append(w)
            if len(pos) is 1:
                dis += math.sqrt(((x[pos[0]]-x[la])^2)+((y[pos[0]]-y[la])^2))
                la = pos[0]
            else:
                dd = []
                for z in pos:
                    qw = math.sqrt(((x[z]-x[la])^2)+((y[z]-y[la])^2))
                    dd.append(qw)
                mi = dd.index(min(dd))
                dis += dd[mi]
                la = pos[mi]
            for w in range(0,k):
                    if a[w] is 1 and s[la][w] is '1':
                        a[w] = 2
        dis += math.sqrt(((x[la])^2)+((y[la])^2))
        print(dis)
