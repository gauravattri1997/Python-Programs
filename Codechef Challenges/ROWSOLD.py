t = int(input())
for i in range(0,t):
    a = input()
    n = 0
    while '10' in a:
        b = a.index('10')
        if '01' in a[b:]:
            c = a[b:].index('01')
            a = a[:b]+'0'+a[b+1:b+c]+'1'+a[b+c+1:]
        else:
            c = len(a[b:])-1
            a = a[:b]+'0'+a[b+1:b+c]+'1'
        n += 1+c
    print(n)
