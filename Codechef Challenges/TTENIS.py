t = int(input())
for i in range(0,t):
    s = input()
    l = len(s)
    m = s.count('0')
    n = s.count('1')
    if l<=20 :
        if n>=11:
            print ('WIN')
        else:
            print ('LOSE')
    else :
        if n-m>=2 :
            print ('WIN')
            continue
        else:
            print ('LOSE')
            continue
