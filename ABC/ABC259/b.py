import math
import cmath

a, b, d = map(int, input().split())


z = cmath.rect(1, math.radians(d))

p = complex(a, b)

ans = p*z
print(ans.real, ans.imag)
