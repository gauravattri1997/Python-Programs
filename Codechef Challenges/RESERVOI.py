t=int(input())
for i in range(0,t):
    n,m = map(int,input().split())
    a = []
    z = 0
    for j in range(0,n):
        a.extend(map(str,input()))
    for j in range(0,m):
        if a[m*n-m+j]!='B':
            z = 1
            break
    else:
        for k in range(0,n-1):
            if a[m*k]!='B' or a[m*k+m-1]!='B':
                z = 1
                break
        else:
            if 'A' in a:
                b = a.index('A')-m
                while b>0:
                    if a[b]!='A':
                        z = 1
                        break
                    b = b-m
                else:
                    if 'W' in a:
                        c = a.index('W')
                        if a[c-1]=='A' or a[c+1]=='A':
                            z = 1
    if z==0:
        print('yes')
    else:
        print('no')
