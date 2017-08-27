def fin(w):
    global a,c,p,q,r,d,e
    st,en = 0,p-1
    d = int((st+en)/2)
    while st is not en:
        if a[d]<w:
            st = d+1
        else:
            en = d
        d = int((st+en)/2)
    if d<p-1 and a[d+1]<=w:
        d += 1
    st,en = 0,r-1
    e = int((st+en)/2)
    while st is not en:
        if c[e]<w:
            st = e+1
        else:
            en = e
        e = int((st+en)/2)
    if e<r-1 and c[e+1]<=w:
        e += 1           

t = int(input())
for i in range(0,t):
    d,e,sum = 0,0,0
    p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    a.sort()
    c.sort()
    for y in b:
        fin(y)
        for x in a[:d+1]:
            for z in c[:e+1]:
                sum += (x+y)*(y+z)
    print(sum%1000000007)
