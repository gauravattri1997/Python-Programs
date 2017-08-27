n=int(input())
for i in range(0,n):
    s = str(input())
    l = len(s)
    for x in s:
        c = 2*(s.count(x))
        if(c==l):
            n=1
            break
        else:
            n=0
    if(n==1):
        print('YES')
    else:
        print('NO')
