n = int(input())
for i in range(0,n):
    c,d,l = map(int,input().split())
    if l%4==0:
        a = int(l/4)
        if c<=d*2:
            if d<=a and a<=d+c:
                print("yes")
            else:
                print("no")
        else:
            p = int(c-2*d)
            if d+p<=a and a<=d+c:
                print("yes")
            else:
                print("no")
    else:
        print("no")
