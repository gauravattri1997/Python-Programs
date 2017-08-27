t = int(input())
for i in range(0,t):
    count=0
    a,b,c,d = map(int,input().split())
    a,b,c,d = min(a,b),max(a,b),min(c,d),max(c,d)
    if(a+1<c):
        if(b+1<c):
            count = (b-a+1)*(d-c+1)
        elif(b+2>d):
            count = (d-c+1)*(c-a-1)+(d-c+1)*(d-c+2)/2
        else:
            count = (d-c+1)*(c-a-1)+(d-c+1)*(d-c+2)/2-(d-b-1)*(d-b)/2
    else:
        count = (d-a)*(d-a+1)/2
        if(b<d):
            count -= (d-b-1)*(d-b)/2
    print(int(count))
