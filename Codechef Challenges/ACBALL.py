t = int(input())
for i in range(0,t):
    x = str(input())
    y = str(input())
    n = len(x)
    a = []
    for k in range(0,n):
        if x[k]=='B' and y[k]=='B' :
            a.append('W')
        else :
            a.append('B')
    z = "".join(a)
    print(z)
    
