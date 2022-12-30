N = int(input())
S = input()
dp = [[0]*10 for _ in range(1 << 10)]
dp[0][0] = 1
alp = 'ABCDEFGHIJ'
MOD = 998244353
for i in range(N):
    idx = alp.index(S[i])
    dp1 = [[0]*10 for _ in range(1 << 10)]
    for s in range(1 << 10):
        if not s & (1 << idx):
            for u in range(10):
                dp1[s | (1 << idx)][idx] += dp[s][u]
        else:
            dp1[s][idx] += dp[s][idx]

        for v in range(10):
            dp1[s][v] += dp[s][v]
            dp1[s][v] %= MOD
    dp = dp1

ans = 0
for s in range(1, 1 << 10):
    ans += sum(dp[s])
    ans %= MOD
print(ans)
