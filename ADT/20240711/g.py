def f(a, b, x):
    return b * x + a / ((1 + x) ** 0.5)


A, B = map(int, input().split())

l, r = 0, 1 << 60
while l + 2 < r:
    c1 = l + (r - l) // 3
    c2 = r - (r - l) // 3
    if f(A, B, c1) < f(A, B, c2):
        r = c2
    else:
        l = c1
ans = 1 << 60
for t in range(l, r + 1):
    ans = min(ans, f(A, B, t))
print(ans)
