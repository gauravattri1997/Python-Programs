t=int(input())
for x in range(t):
    a,c = [1],0
    b = input()
    for i in b:
        if i is '<':
            a.append(a[c]+1)
        elif i is '>':
            a.append(a[c]-1)
        else:
            a.append(a[c])
        c += 1
    n = max(a)-min(a)+1
    print(n)
