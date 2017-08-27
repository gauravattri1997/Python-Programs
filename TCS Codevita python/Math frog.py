n=int(input())
count,p,f,b,d=1,[],[],[],[]
for i in range(n):
    p.append(list(map(int,input().split(','))))
for i in range(2):
    f.append(list(map(int,input().split(','))))
a,c=f[0],[f[0]]
for i in range(a[1],n):
    if p[a[0]-1][i] is 1:
        b.append([a[0],i+1])
        break
for i in range(a[0],n):
    if p[i][a[1]-1] is 1:
        b.append([i+1,a[1]])
        break
for i in range(a[1]-2,-1,-1):
    if p[a[0]-1][i] is 1:
        b.append([a[0],i+1])
        break
for i in range(a[0]-2,-1,-1):
    if p[i][a[1]-1] is 1:
        b.append([i+1,a[1]])
        break
s=b.copy()
b.clear()
while f[1] not in s:
    temp=s.copy()
    d=s.copy()
    s.clear()
    count += 1
    while temp:
        a=temp.pop(0)
        for i in range(a[1],n):
            if p[a[0]-1][i] is 1:
                b.append([a[0],i+1])
                break
        for i in range(a[0],n):
            if p[i][a[1]-1] is 1:
                b.append([i+1,a[1]])
                break
        for i in range(a[1]-2,-1,-1):
            if p[a[0]-1][i] is 1:
                b.append([a[0],i+1])
                break
        for i in range(a[0]-2,-1,-1):
            if p[i][a[1]-1] is 1:
                b.append([i+1,a[1]])
                break
    for i in b:
        if i not in s:
            s.append(i)
    b.clear()
    for i in c:
        if i in s:
            s.remove(i)
    c=d.copy()
print(count)
