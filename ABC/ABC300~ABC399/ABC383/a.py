from collections import defaultdict

N = int(input())
d = defaultdict(lambda: -1)
last = -1
for i in range(N):
    t, v = map(int, input().split())
    d[t] = v
    if i == N - 1:
        last = t
ans = 0
for t in range(1, last + 1):
    if ans:
        ans -= 1
    if d[t] != -1:
        ans += d[t]

print(ans)
