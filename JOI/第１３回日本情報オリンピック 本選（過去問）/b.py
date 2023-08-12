from itertools import accumulate
M, N = map(int, input().split())
P = [int(input()) for _ in range(M)]
INF = 1 << 60
dp = [INF]*(M+1)
dp[0] = 0
for _ in range(N):
    C, E = map(int, input().split())
    for j in range(M, -1, -1):
        dp[j] = min(dp[j], dp[max(0, j-C)]+E)
CUMSUM = list(accumulate([0]+sorted(P)[::-1]))
ans = 0
for i in range(M+1):
    ans = max(ans, CUMSUM[i]-dp[i])
print(ans)
