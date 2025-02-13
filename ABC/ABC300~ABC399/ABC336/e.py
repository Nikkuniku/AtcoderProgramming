N = int(input())
M = str(N)
L = len(M)
K = 9 * 14
dp = [
    [[[[0] * (K + 1) for _ in range(K + 1)] for _ in range(K + 1)] for _ in range(2)]
    for _ in range(L + 1)
]
for k in range(K):
    dp[0][0][0][k][0] = 1
for i in range(L):
    for smaller in range(2):
        Limit = 10 if smaller == 1 else int(M[i]) + 1
        for d in range(K):
            for e in range(1, K):
                for m in range(e):
                    for x in range(Limit):
                        if d + x >= K:
                            continue
                        dp[i + 1][smaller | (x < int(M[i]))][d + x][e][
                            (10 * m + x) % e
                        ] += dp[i][smaller][d][e][m]
ans = 0
for D in range(K):
    ans += dp[L][0][D][D][0]
    ans += dp[L][1][D][D][0]
print(ans)
