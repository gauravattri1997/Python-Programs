def chle(val,pos):
    global score,h
    while pos>=1 and h[pos-1] is not val-1:
        val -= 1
        pos -= 1
        score += h[pos]-val
        h[pos] = val

def chri(val,pos):
    global score,h
    while pos<=n-2 and h[pos+1] is not val-1:
        val -= 1
        pos += 1
        score += h[pos]-val
        h[pos] = val

t = int(input())
for i in range(0,t):
    n = int(input())
    h = list(map(int,input().split()))
    a,b,c,score = 0,n-1,1,0
    while a<b:
        if h[a]>c:
            score += h[a]-c
            h[a] = c
        elif h[a]<c:
            c = h[a]
            chle(c,a)
            a += 1
            c += 1
            continue
        a += 1
        if h[b]>c:
            score += h[b]-c
            h[b] = c
        elif h[b]<c:
            c = h[b]
            chri(c,b)
            b -= 1
            c += 1
            continue
        b -= 1
        c += 1
    if h[a]>c:
        score += h[a]-c
        h[a] = c
    elif h[a]<c:
        c = h[a]
        chle(c,a)
        chri(c,a)
    print(score)
