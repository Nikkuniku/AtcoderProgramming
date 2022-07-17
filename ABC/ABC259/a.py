n, m, x, t, d = map(int, input().split())

ans = t
for i in range(n, -1, -1):
    if i == m:
        break
    if x < i <= n:
        continue
    ans -= d
print(ans)
