a = int(input())
b = int(input())
c = int(input())
ans = "No"
for x in range(1, 200):
    for y in range(1, 200):
        z = x + y + a
        if not z < b + c:
            continue
        if not b < c + z:
            continue
        if not c < b + z:
            continue
        cosB = (b**2 + z**2 - c**2) / (2 * b * z)
        p = (b**2 + x**2 - 2 * b * x * cosB) ** 0.5
        costheta = (b**2 + p**2 - x**2) / (2 * b * p)
        cosC = (c**2 + z**2 - b**2) / (2 * c * z)
        q = (c**2 + y**2 - 2 * c * y * cosC) ** 0.5
        cosphi = (c**2 + q**2 - y**2) / (2 * c * q)
        EPS = 10 ** (-6)
        if abs(costheta - cosphi) < EPS:
            ans = "Yes"
print(ans)
