t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    hap,p,q=0,0,0
    for x in a:
        if x<0:
            hap += x
        else:
            p += 1
            q += x
    hap += p*q
    print(hap)
