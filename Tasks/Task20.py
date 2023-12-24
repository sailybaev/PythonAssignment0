import math

x,y,z = map(float , input().split())

a = (3 + math.e ** (y-1)) / (1 + x**2 * (abs(y - math.tan(z))))
b = 1 + abs(y-x) + ((y-x)**2)/2 + (abs(y-x) ** 3)/3