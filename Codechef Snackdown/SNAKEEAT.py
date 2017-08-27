t=int(input())
for i in range(0,t):
    n,q = map(int,input().split())
    l = list(map(int,input().split()))
    k = []
    l.sort(reverse=True)
    for j in range(0,q):
        k.append(int(input()))
        le = l.copy()
        li = []
        while le:
            if le[0]>=k[j]:
                li.append(le[0])
                le.pop(0)
            else:
                le[0] += 1
                le.pop()
        print(len(li))
