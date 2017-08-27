def chsn(j):
    global st,ot,n
    st = st[:j]+'.'+st[j+1:]
    j += 1
    while j<n and st[j] is '#':
        st = st[:j]+'.'+st[j+1:]
        if ot[j] is '#':
            st,ot = ot,st
        else:
            j += 1

t = int(input())
for i in range(0,t):
    n = int(input())
    a = input()
    b = input()
    j,c = 0,0
    while a[j] is not '#' and b[j] is not '#':
        j += 1
    if a[j] is '#':
        st,ot = a,b
        chsn(j)
        if b[j] is '#':
            if ot[j] is '#':
                st,ot = ot,st
            st = st[:j]+'.'+st[j+1:]
            j -= 1
            while st[j] is '#' and j>=0:
                st = st[:j]+'.'+st[j+1:]
                if ot[j] is '#':
                    st,ot = ot,st
                else:
                    j -= 1
    else:
        st,ot = b,a
        chsn(j)
    if ('#' in st) or ('#' in ot):
        print('no')
    else:
        print('yes')
