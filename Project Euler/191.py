N = 30
M = 4
L = 3
dp = [[[0] * L for _ in range(M)] for _ in range(N + 1)]
dp[0][0][0] = 1
for i in range(N):
    for j in range(M):
        for k in range(L):
            # Absent
            dp[i + 1][min(j + 1, M - 1)][k] += dp[i][j][k]
            # on time
            if j <= 2 and k <= 1:
                dp[i + 1][0][k] += dp[i][j][k]
            # late
            if j <= 2 and k <= 1:
                dp[i + 1][0][min(k + 1, L - 1)] += dp[i][j][k]
ans = 0
for j in range(M):
    if j == 3:
        continue
    for k in range(L):
        if k == 2:
            continue
        ans += dp[N][j][k]
print(ans)
