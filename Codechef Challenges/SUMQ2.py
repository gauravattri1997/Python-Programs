def f(x,y,z):
    if x>y or y<z:
        return 0
    else:
        return (x+y)*(y+z)

t = int(input())
for i in range(0,t):
    sum = 0
    p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    for y in b:
        for x in a:
            for z in c:
                sum += f(x,y,z)
    print(sum%1000000007)
