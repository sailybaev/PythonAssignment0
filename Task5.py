import math

a,b = map(int , input().split())
c = math.sqrt((a**2) + (b**2))
P = a+b+c
print(P)