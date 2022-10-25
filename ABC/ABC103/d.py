n, m = map(int, input().split())
interval = [tuple(map(int, input().split())) for _ in range(m)]
interval.sort(key=lambda x: x[1])
ans = 0
l, r = -1, -1
for i in range(m):
    a, b = interval[i]
    if r <= a:
        ans += 1
        r = b
print(ans)
