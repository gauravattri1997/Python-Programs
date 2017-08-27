from itertools import permutations

s=input()
b=[]
n=len(s)
if n%2 is 0:
    m=''
else:
    m=s[int(n/2)]
a=s[:int(n/2)]
perm = permutations(sorted(a))
for i in list(perm):
    q=''.join(i)
    st = q+m+q[::-1]
    if st not in b:
        b.append(st)
for i in b:
    print(i)
