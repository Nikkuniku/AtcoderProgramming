H, W, K = map(int, input().split())
sx, sy, gx, gy = map(int, input().split())
dp = [[0]*4 for _ in range(K+1)]
if sx == gx and sy == gy:
    dp[0][0] = 1
elif sx == gx and sy != gy:
    dp[0][1] = 1
elif sx != gx and sy == gy:
    dp[0][2] = 1
else:
    dp[0][3] = 1
MOD = 998244353
for i in range(K):
    dp[i+1][0] = (dp[i][1]+dp[i][2]) % MOD
    dp[i+1][1] = ((W-1)*dp[i][0]+(W-2)*dp[i][1]+dp[i][3]) % MOD
    dp[i+1][2] = ((H-1)*dp[i][0]+(H-2)*dp[i][2]+dp[i][3]) % MOD
    dp[i+1][3] = ((H-1)*dp[i][1]+(W-1)*dp[i][2]+(H+W-4)*dp[i][3]) % MOD
print(dp[K][0])
