t = int(input())
for i in range(0,t):
    a = list(input())
    a.append('a')
    if a[0] is 'm' and a[1] is 's':
        a[1] = 'a'
    n = len(a)
    j = 1
    while 'm' in a[j:]:
        k = a[j:].index('m')
        if a[j+k-1] is 's':
            a[j+k-1] = 'a'
        elif j+k+1 < n and a[j+k+1] is 's':
            a[j+k+1] = 'a'
        j += k+1
    sn = a.count('s')
    mo = a.count('m')
    if sn<mo:
        print('mongooses')
    elif sn>mo:
        print('snakes')
    else:
        print('tie')
