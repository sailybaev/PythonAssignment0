import math

x1,y1,x2,y2,x3,y3 = map(float , input().split())

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

P = a+b+c

print(P)