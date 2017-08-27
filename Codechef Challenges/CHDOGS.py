t = int(input())
for i in range(0,t):
    s,v = map(int,input().split())
    a = s/(v*(3**(.5)))
    a = round(a,7)
    print (a)
