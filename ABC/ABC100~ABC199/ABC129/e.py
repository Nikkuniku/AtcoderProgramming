L = input()
N = len(L)
dp = [[[0, 0] for _ in range(2)] for _ in range(N+1)]
dp[0][0][0] = 1
MOD = 10**9 + 7
for i in range(N):
    p = int(L[i])
    for smaller in range(2):
        limit = 2 if smaller else p+1
        for x in range(limit):
            cor = 2 if x == 1 else 1
            dp[i+1][smaller | (x < p)][x] += sum(dp[i][smaller])*cor
            dp[i+1][smaller | (x < p)][x] %= MOD
ans = sum(sum(dp[N], [])) % MOD
print(ans)
