t = int(input())
for i in range(0,t):
    n,k = map(int,input().split())
    s = input()
    co = 0
    b = -1
    v = s.count('a')
    for j in range(0,v):
        b += 1+s[b+1:].index('a')
        x = s[:b+1].count('b')
        y = s[b+1:].count('b')
        co += k*(x*(k-1)+y*(k+1))/2
    print(co)
