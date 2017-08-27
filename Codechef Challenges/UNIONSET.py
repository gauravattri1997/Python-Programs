from itertools import combinations

t=int(input())
for i in range(0,t):
    n,k = map(int,input().split())
    lst = []
    for j in range(0,n):
        temp = list(map(int,input().split()))
        temp.pop(0)
        lst.append(temp)
    comb = list(combinations(range(0,n),2))
    count = 0
    k1 = set(range(1,k+1))
    for x in comb:
        if set(lst[x[0]]+lst[x[1]]) == k1:
            count += 1
    print(count)
