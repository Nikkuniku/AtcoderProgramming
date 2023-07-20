from bisect import bisect_left
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
pos = [-1]*(N+1)

INF = 1 << 62
dp = [INF]*N
for i, v in enumerate(Q):
    pos[v] = i

for e in P:
    multiple_pos = []
    for j in range(e, N+1, e):
        multiple_pos.append(pos[j])
    multiple_pos.sort(reverse=True)
    for c in multiple_pos:
        dp[bisect_left(dp, c)] = c
ans = bisect_left(dp, INF)
print(ans)
