W, H = map(int, input().split())
MOD = 100000
dp = [[[[0, 0], [0, 0]] for _ in range(W)] for _ in range(H)]
for i in range(H):
    dp[i][0][0][0] = 1
for j in range(W):
    dp[0][j][1][0] = 1
for i in range(1, H):
    for j in range(1, W):
        for k in range(2):
            dp[i][j][k][0] = sum(dp[i-(1-k)][j-k][k]) % MOD
            dp[i][j][k][1] = dp[i-(1-k)][j-k][1-k][0] % MOD
ans = (sum(dp[H-1][W-1][0])+sum(dp[H-1][W-1][1])) % MOD
print(ans)
