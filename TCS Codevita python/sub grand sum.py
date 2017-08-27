def fib(x):
	if x > 2:
		return fib(x-1)+fib(x-2)
	else:
		return 1

r,c,n=map(int,input().split())
a,b,t=[],[],[]
for i in range(r):
	a.append(list(map(int,input().split())))
for i in range(n):
	b.append(list(map(int,input().split())))
while b:
	t=b.pop()
	s=0
	for i in range(t[0],t[2]+1):
		for j in range(t[1],t[3]+1):
			s += a[i][j]
	t.clear()
	print(fib(s%50))