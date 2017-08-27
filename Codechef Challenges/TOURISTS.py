n,e = map(int,input().split())
a=[]
start,p = 0,0
for i in range(0,e):
    a.append(list(map(int,input().split())))
if a[0][0] in a[e-1]:
    start = a[0][0]
elif a[0][1] in a[e-1] and start!=0:
    start = a[0][1]
    a[0].reverse()
else:
    print('NO')
if start != 0:
    for i in range(1,e):
        if a[i-1][1]==a[i][1]:
            a[i].reverse()
        elif a[i-1][1] in a[i] == False:
            p = 1
            print('NO')
            break
    if p==0:
        print('YES')
        for i in range(0,e):
            print(a[i][0],a[i][1])
