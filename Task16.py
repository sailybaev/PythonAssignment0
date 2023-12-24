x , y = map(float , input().split())

q = (abs(x) + abs(y)) / (1 + abs(x*y))

print(q)
