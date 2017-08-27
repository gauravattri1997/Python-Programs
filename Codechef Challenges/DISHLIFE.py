t = int(input())
for j in range(0,t):
    n,k = map(int,input().split())
    p=[]
    a=[]
    count,m=0,0
    for i in range(0,n):
        p.append(list(map(int,input().split())))
        a.extend(p[i][1:])
    for i in range(1,k+1):
        if i not in a:
            count=1
            break
        else:
            for k in range(0,n):
                p[k][1:].remove(i)
    if count==1:
        print("sad")
    else:
        for i in range(0,n):
            count=0
            for k in range(1,p[i][0]+1):
                if a.count(p[i][k])>=2:
                    count += 1
            if count==p[i][0]:
                m = 1
                break
        if m==1:
            print("some")
        else:
            print("all")
