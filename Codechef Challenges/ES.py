import math

n = int(input())
sm = 0
d = format(math.e,'.100g')
e = int('2'+d[2:])
for x in range(1,n+1):
    sm += int((n*e)/10**51)
print(sm)
a,b = divmod(n,7)

