from collections import defaultdict

N = int(input())
d = defaultdict(int)
last = -1
for i in range(N):
    t, v = map(int, input().split())
    if i == N - 1:
        last = t
    d[t] = v
ans = 0
now = 1
for t in range(1, last + 1):
    ans += d[t]
    if t < last and ans > 0:
        ans -= 1
print(ans)
