n = int(input())

ans = []
for x in range(1, n+1):
    for y in range(1, min(x**2, n) + 1):
        p = x**2 - y

        for k in range(2, n+1):
            if p % (k**2) == 0:
                p //= k**2

        if p == 1:
            ans.append((x, y, x**2 - y))
        elif p == 0:
            ans.append((x, y, x**2 - y))

print(*ans)
