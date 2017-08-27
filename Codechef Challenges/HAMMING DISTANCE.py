def hamdis(a,b):
    p=0
    l=len(a)
    for j in range(0,l):
        if(a[j]==b[j]):
            p += 1
    return p
