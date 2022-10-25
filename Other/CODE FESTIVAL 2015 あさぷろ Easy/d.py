n = int(input())
S = input()


def LCS(s, t):
    n, m = len(s), len(t)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
            if s[i] == t[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
    return dp[n][m]


ans = n+1
for i in range(n):
    a = S[:i]
    b = S[i:]
    tmp = LCS(a, b)
    ans = min(ans, n-2*tmp)
print(ans)
