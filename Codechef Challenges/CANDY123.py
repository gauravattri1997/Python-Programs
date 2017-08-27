t=int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    x,y = 0,0
    m,n = 1,2
    while x<=a and y<=b:
        x += m
        y += n
        m += 2
        n += 2
    if x>a:
        print("Bob")
    else:
        print("Limak")
