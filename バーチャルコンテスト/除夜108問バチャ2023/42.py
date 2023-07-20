from math import radians, sin, cos
a, b, d = map(int, input().split())
z = complex(a, b)
d = radians(d)
w = complex(cos(d), sin(d))
z *= w
print(z.real, z.imag)
