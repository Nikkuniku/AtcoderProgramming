R, C, K = map(int, input().split())
val = [[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    val[r][c] = v
INF = 0
dp = [[[0]*(C+1)for _ in range(R+1)] for _ in range(4)]
dp[0][0][0] = 0
for i in range(R+1):
    for j in range(C+1):
        if i == 0 and j == 0:
            continue
        if j-1 >= 0:
            for k in range(4):
                # 取らない
                dp[k][i][j] = max(dp[k][i][j], dp[k][i][j-1])
                # 取る
                if 0 <= k-1 <= 2:
                    dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j-1]+val[i][j])
        if i-1 >= 0:
            for k in range(4):
                # 取らない
                dp[0][i][j] = max(dp[0][i][j], dp[k][i-1][j])
                # 取る
                if val[i][j] > 0:
                    dp[1][i][j] = max(dp[1][i][j], dp[k][i-1][j]+val[i][j])
ans = 0
for k in range(4):
    ans = max(ans, dp[k][R][C])
print(ans)
