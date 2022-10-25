N, L = map(int, input().split())
X = set(map(int, input().split()))
t1, t2, t3 = map(int, input().split())
INF = 1 << 62
dp = [[INF]*(L+6) for _ in range(2)]
dp[0][0] = 0
for i in range(L+1):
    dp[0][i+1] = min(dp[0][i+1], dp[0][i]+t1 + (t3 if i in X else 0))
    dp[1][i+1] = min(dp[1][i+1], dp[0][i]+(t1//2) +
                     (t2//2) + (t3 if i in X else 0))

    dp[0][i+2] = min(dp[0][i+2], dp[0][i]+t1+t2+(t3 if i in X else 0))
    dp[1][i+2] = min(dp[1][i+2], dp[0][i]+(t1//2) +
                     (3*t2//2)+(t3 if i in X else 0))

    dp[1][i+3] = min(dp[1][i+3], dp[0][i]+(t1//2) +
                     (5*t2//2)+(t3 if i in X else 0))
    dp[0][i+4] = min(dp[0][i+4], dp[0][i]+t1+3*t2+(t3 if i in X else 0))

print(min(dp[0][L], dp[1][L]))
