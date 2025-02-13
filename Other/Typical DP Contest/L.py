N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
dp = [[-(1 << 18)] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0
ma = [0] * (N + 1)
for i in range(N):
    csum = 0
    for j in range(i, -1, -1):
        csum += F[i][j]
        dp[i + 1][j] = max(dp[i + 1][j], ma[j] + 2 * csum)
    ma = [-(1 << 18)] * (N + 1)
    for j in range(N + 1):
        if j != 0:
            ma[j] = max(ma[j], ma[j - 1])
        ma[j] = max(ma[j], dp[i + 1][j])
print(max(dp[N]))
