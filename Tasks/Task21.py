import math

x,y,z = map(float , input().split())

a = (1+y) * (x+y / (x**2 + 4)) / (math.e ** (-x-2) + 1 / (x**2 + 4))
b = (1 + math.cos(y-2)) / (x**4 / 2 + math.sin(z)**2)

