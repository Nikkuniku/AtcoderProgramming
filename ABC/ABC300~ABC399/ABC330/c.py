D = int(input())
ans = 1 << 60
for x in range(D):
    if x**2 > D:
        break
    l = 0
    r = int(D ** (1 / 2)) + 1
    p = x**2
    while r - l > 1:
        mid = (l + r) // 2
        if mid**2 + p - D >= 0:
            r = mid
        else:
            l = mid
    if l >= 0:
        ans = min(ans, abs(l**2 + p - D))
    if r >= 0:
        ans = min(ans, abs(r**2 + p - D))
print(ans)
