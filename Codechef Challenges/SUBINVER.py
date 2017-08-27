n,u = map(int,input().split())
s = ['0'*n]
a = ['1','0']
for i in range(1,u+1):
    l1,r1 = map(int,input().split())
    st = s[i-1]
    su = st[l1-1:r1]
    for j in su:
        su += a[int(j)]
    st = st[:l1-1] + su[r1-l1+1:] + st[r1:]
    s.append(st)
print(max(s))
