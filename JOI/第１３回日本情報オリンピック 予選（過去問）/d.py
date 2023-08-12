N = int(input())
S = input()
JOI = 'JOI'
MOD = 10007
dp = [[0]*(1 << 3)for _ in range(N+1)]
# 初期値
t = JOI.index(S[0])
for s in range(1 << 3):
    if (s & (1 << 0)) and (s & (1 << t)):
        dp[1][s] = 1
for i in range(1, N):
    t = JOI.index(S[i])
    for k in range(1 << 3):
        for s in range(1 << 3):
            isOK = False
            for j in range(3):
                if (k & (1 << t)) != 0 and (k & (1 << j)) != 0 and (s & (1 << j)) != 0:
                    isOK = True
            if isOK:
                dp[i+1][k] += dp[i][s]
                dp[i+1][k] %= MOD
ans = sum(dp[N]) % MOD
print(ans)
