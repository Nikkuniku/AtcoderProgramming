N, M = map(int, input().split())
INF = 1000_000_000_000_000_00

dp = [INF]*(1 << N)
dp[0] = 0
for i in range(M):
    si, ci = input().split()
    tmp = 0
    for j in range(N):
        if si[j] == 'Y':
            tmp |= (1 << j)
    for s in range(1 << N):
        dp[s | tmp] = min(dp[s | tmp], dp[s]+int(ci))

ans = dp[(1 << N)-1]
if ans == INF:
    ans=-1
print(ans)
