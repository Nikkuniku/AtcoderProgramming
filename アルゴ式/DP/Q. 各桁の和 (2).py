N, A, B = map(int, input().split())
M = len(str(N))
dp = [[[[0]*B for _ in range(A)] for _ in range(2)] for _ in range(M+1)]
dp[0][0][0][0] = 1
for i in range(M):
    p = int(str(N)[i])
    for smaller in range(2):
        lim = 10 if smaller else p+1
        for d in range(A):
            for r in range(B):
                for x in range(lim):
                    dp[i+1][smaller | (x < p)][(d+x) %
                                               A][(10*r+x) % B] += dp[i][smaller][d][r]
ans = -1
for smaller in range(2):
    ans += dp[M][smaller][0][0]
print(ans)
