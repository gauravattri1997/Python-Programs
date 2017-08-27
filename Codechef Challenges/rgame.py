def s(i):
    if(i==1):
        return 2*a[0]*a[1]
    else:
        return (a[i]*(s(i-1)/a[i-1]+(2**(i-1))*a[i-1]))
global a
a = []
t = int(input())
for j in range(0,t):
    value = 0
    n = int(input())
    a[:] = list(map(int,input().split()))
    for k in range(1,n+1):
        value += ((2**(n-k))*s(k))
    a.clear()
    value = value % 1000000007
    print(int(value))
