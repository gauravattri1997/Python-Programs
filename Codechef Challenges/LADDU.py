t = int(input())
for i in range(0,t):
    t = 0
    s = input().split(' ')
    for x in range(0,int(s[0])):
        a = input().split(' ')
        if 'CONTEST_WON' in a:
            t += 300
            if int(a[1])<20 :
                t += 20-int(a[1])
        if 'TOP_CONTRIBUTOR' in a:
            t += 300
        if 'BUG_FOUND' in a:
            t += int(a[1])
        if 'CONTEST_HOSTED' in a:
            t += 50
    if(s[1]=='INDIAN'):
        print(int(t/200))
    else :
        print(int(t/400))
