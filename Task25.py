import math

x,y,z = map(float , input().split())

a = math.log( abs(  (y - math.sqrt( abs(x)) )  * (x - (y / z+x**2/4))) )
b = x - (x**2) / math.factorial(3) + (x**5) / math.factorial(5)

