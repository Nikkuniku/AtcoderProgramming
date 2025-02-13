from math import sqrt, floor
from fractions import Fraction

root = sqrt(3)
Period = []
seen_decimal = set()
while 1:
    a = floor(root)
    Period.append(a)
    z = root - a
    if z in seen_decimal:
        break
    seen_decimal.add(z)
    root = 1 / z
print(Period)
