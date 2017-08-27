t=int(input())
for i in range(0,t):
    name = list(input().split())
    j = len(name)-1
    new = name[j].title()
    j-=1
    while(j>=0):
        name[j] = name[j].title()
        new = name[j][0] + '. ' + new
        j-=1
    print(new)
