N, T = map(int, input().split())
ans = 1 << 60
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
if ans == 1 << 60:
    ans = 'TLE'
print(ans)
