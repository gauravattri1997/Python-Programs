n=int(input())
a,b = 3,2
for i in range(1,n+1):
    for j in range(0,i):
        print('{:d}'.format(a*b).zfill(5),end=' ')
        a += 4
        b += 2
    print('')
