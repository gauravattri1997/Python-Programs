t = int(input())
for z in range(0,t):
    n,m = map(int,input().split())
    a,ma = [],1
    for i in range(0,n):
        a.append(list(map(int,input().split())))
        ma = max(ma,max(a[i]))
    h,x,co,po = 0,n*m,0,[]
    for i in range(0,n):
        co += a[i].count(ma) 
    while co is not x:
        for i in range(0,n):
            for j in range(0,m):
                if a[i][j] is ma:
                    po.append([i,j])
        while po:
            getpo = po.pop()
            ia,ja = getpo[0],getpo[1]
            
        
