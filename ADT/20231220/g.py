A, B = map(int, input().split())


def f(x):
    return x * B + (A / (1 + x) ** (0.5))


low = 0
high = 1 << 60
for _ in range(300):
    c1 = (2 * low + high) // 3
    c2 = (low + 2 * high) // 3
    if f(c1) > f(c2):
        low = c1
    else:
        high = c2
ans = 1 << 60
for i in range(low, high + 1):
    ans = min(ans, f(i))
print(ans)
