def qwerty():
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split(' ')))
        b=[0,0,0,0,0,0,0]
        j=a[0]
        if 7 in a:
            while j is not 7:
                b[a[0]-1] += 1
                j = a.pop(0)
            b[6] -= 1
            while a[0] is 7:
                a.pop(0)
            while a:
                b[a.pop(0)-1] -= 1
            if b.count(0) is 7:
                print('yes')
            else:
                print('no')
        else:
            print('no')
    return 0

if __name__=="__main__":
    qwerty()
