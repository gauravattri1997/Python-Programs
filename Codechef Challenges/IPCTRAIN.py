def srt():
    global lst,n
    for i in range(1,n):
        m,j = lst[i],i-1
        while j is not -1:
            if m[2]<lst[j][2]:
                m,lst[j] = lst[j],m
            j -= 1
        lst[i] = m

t=int(input())
lst = []
for x in range(t):
    n,d=map(int,input().split())
    for y in range(n):
        lst.append(list(map(int,input().split())))
    count,dt=0,d
    srt()
    while dt>=0:
        
    print(lst)
    lst.clear()
