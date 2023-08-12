S = input()
N = len(S)
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
MOD = 998244353
for i in range(N):
    s = S[i]
    for j in range(N+1):
        if s == '(' or s == '?':
            if j+1 <= N:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
        if s == ')' or s == '?':
            if j-1 >= 0:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= MOD
ans = dp[N][0]
print(ans)
