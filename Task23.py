import math

x,y,z = map(float , input().split())

a = (math.cos(x - math.pi / 6) * 2) / (1/2 + math.sin(y)**2)
b = 1 + (z**2 / (3+z**2 / 5))

