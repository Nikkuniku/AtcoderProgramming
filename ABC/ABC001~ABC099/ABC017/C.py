from itertools import accumulate

N, M = map(int, input().split())
S = 0
V = [0] * (M + 2)
for _ in range(N):
    l, r, s = map(int, input().split())
    S += s
    V[l] += s
    V[r + 1] -= s
cum = list(accumulate(V))
ans = 0
for i in range(1, M + 1):
    ans = max(ans, S - cum[i])
print(ans)
