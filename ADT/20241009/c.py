from math import sin, cos, pi

a, b, d = map(int, input().split())
d = d * pi / 180
x = a * cos(d) - b * sin(d)
y = a * sin(d) + b * cos(d)
print(x, y)
