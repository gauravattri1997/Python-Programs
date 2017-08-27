n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mi,ma = min(b),max(b)
if max(abs(mi),abs(ma)) is ma:
    ind = b.index(ma)
    a[ind] -= 2*k
else:
    ind = b.index(mi)
    a[ind] += 2*k
s = 0
for i in range(0,n):
    s += a[i]*b[i]
print(s)
