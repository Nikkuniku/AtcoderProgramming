M, N = map(int, input().split())
X = list(map(int, input().split()))
bit = [0] * M
for j in range(M):
    tmp = 0
    for k in range(M):
        if X[k] - 1 == j:
            tmp |= 1 << k
    bit[j] = tmp
dp = [[0] * (1 << M) for _ in range(N + 1)]
dp[0][(1 << M) - 1] = 1
MOD = 998244353
for i in range(N):
    for s in range(1 << M):
        for j in range(M):
            if not s & (1 << j):
                continue
            dp[i + 1][(s ^ (1 << j)) | bit[j]] += dp[i][s]
            dp[i + 1][(s ^ (1 << j)) | bit[j]] %= MOD
ans = sum(dp[-1]) % MOD
print(ans)
