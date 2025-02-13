N, M = map(int, input().split())
cummin = [1e18] * (M + 1)
Seg = [list(map(int, input().split())) for _ in range(N)]
P = [1e18] * (M + 1)
for a, b in Seg:
    P[a] = min(P[a], b)
for i in range(M, 0, -1):
    if i == M:
        cummin[i] = P[i]
    else:
        cummin[i] = min(cummin[i + 1], P[i])
ans = 0
for i in range(1, M + 1):
    if cummin[i] == 1e18:
        ans += M - i + 1
    else:
        ans += cummin[i] - 1 - i + 1
print(ans)
