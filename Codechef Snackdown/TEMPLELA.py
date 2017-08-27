s=int(input())
for i in range(0,s):
    n=int(input())
    h = list(map(int,input().split()))
    ch = 1
    ce = int((n-1)/2)
    if n%2 is not 0:
        k = 0
        while k is not ce:
            if h[k] is k+1 and h[n-k-1] is k+1:
                ch = 1
            else:
                ch = 0
                break
            k += 1
        if ch is 1 and h[ce] is ce+1:
            print('yes')
        else:
            print('no')
    else:
        print('no')
