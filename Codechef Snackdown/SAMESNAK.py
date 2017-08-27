t=int(input())
for i in range(0,t):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if a[0] is a[2]:
        if b[0] is a[0] and b[2] is a[0]:
            if (b[1]>=min(a[1],a[3]) and b[1]<=max(a[1],a[3])) or (b[3]>=min(a[1],a[3]) and b[3]<=max(a[1],a[3])):
                print('yes')
            else:
                print('no')
        elif b[0] is a[0] and (b[1] is a[1] or b[1] is a[3]):
            print('yes')
        elif b[2] is a[0] and (b[3] is a[1] or b[3] is a[3]):
            print('yes')
        else:
            print('no')
    elif a[1] is a[3]:
        if b[1] is a[1] and b[3] is a[1]:
            if (b[0]>=min(a[0],a[2]) and b[0]<=max(a[0],a[2])) or (b[2]>=min(a[0],a[2]) and b[2]<=max(a[0],a[2])):
                print('yes')
            else:
                print('no')
        elif b[1] is a[1] and (b[0] is a[0] or b[0] is a[2]):
            print('yes')
        elif b[3] is a[1] and (b[2] is a[0] or b[2] is a[2]):
            print('yes')
        else:
            print('no')
    else:
        print('no')
