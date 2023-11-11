from math import sqrt

N = int(input())
P = list(map(int, input().split()))
dp = [[0.0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + ((10 / 9) ** j) * P[i - 1])
ans = -(1 << 60)
cum = 0

for k in range(1, N + 1):
    cum = 10 * (1 - (9 / 10) ** k)
    tmp = dp[N][k] * ((9 / 10) ** k) / cum
    tmp -= 1200 / sqrt(k)
    ans = max(ans, tmp)
print(ans)
