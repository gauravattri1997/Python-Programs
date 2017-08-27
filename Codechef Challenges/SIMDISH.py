t = int(input())
for i in range(0,t):
    a = list(input().split())
    b = list(input().split())
    n = 0
    for j in range(0,4):
        if a[j] in b:
            n += 1
    if n>=2:
        print("similar")
    else:
        print("dissimilar")
