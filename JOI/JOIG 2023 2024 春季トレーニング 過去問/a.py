N = int(input())
X = list(map(int, input().split()))
X.sort()
INF = 1 << 60
dp = [INF] * N
dp[0] = 0
for i in range(N):
    if i == 0:
        continue
    if i <= 2:
        dp[i] = dp[i - 1] + X[i] - X[i - 1]
    else:
        dp[i] = min(dp[i - 1], dp[i - 2]) + X[i] - X[i - 1]
print(dp[N - 1])
