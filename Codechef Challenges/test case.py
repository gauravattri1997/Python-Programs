t=int(input())
for m in range(0,t):
    n,q = map(int,input().split())
    l = list(map(int,input().split()))
    k = []
    l.sort(reverse=True)
    for j in range(0,q):
        k.append(int(input()))
        le = l.copy()
        mid = int(n/2)
        start = 0
        end = n-1
        while end is not start+1:
            if le[mid]<k[j]:
                end = mid
            else:
                start = mid
            mid = int((start+end)/2)
        if k[j]>le[0]:
            p = 0
        else:
            p = mid+1
        co = n-1
        while p is not co:
            if le[p]>=k[j]:
                p += 1
            else:
                le[p] += 1
                co -= 1
        print(p)
