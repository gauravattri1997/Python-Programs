t = int(input())
for i in range(0,t):
    n = int(input())
    a,temp,j = [1],[1],2
    while len(a) is not n:
        while j in temp:
            j += 1
        for x in a:
            temp.append(x+j)
        a.append(j)
        temp.append(j)
        j += 1
    for x in a:
        print(x,end=' ')
    print()
