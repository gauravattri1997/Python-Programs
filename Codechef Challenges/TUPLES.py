def gcd(num1,num2):
    nu = min(num1,num2)
    ab = 0
    while ab==0:
        if num1%nu==0 and num2%nu==0:
            ab = nu
        nu = nu-1
    return ab

t = int(input())
for i in range(0,t):
    n = int(input())
    x = list(map(int,input().split()))
    p = 0
    for a in range(0,n):
        for b in range(0,n):
            y1 = (x[a]*x[b])%359999
            for c in range(0,n):
                for d in range(0,n):
                    y2 = (x[c]*x[d])%359999
                    g0 = gcd(y1,y2)
                    if g0==1:
                        p = p+n*n
                        continue
                    for e in range(0,n):
                        for f in range(0,n):
                            y3 = (x[e]*x[f])%359999
                            g = gcd(g0,y3)
                            if g==1:
                                p = p+1
    q = p%1000000007
    print(q)
