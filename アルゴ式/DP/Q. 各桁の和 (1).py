N, A = map(int, input().split())
M = len(str(N))
MOD = 10**9 + 7
dp = [[[0]*A for _ in range(2)] for _ in range(M+1)]
dp[0][0][0] = 1
for i in range(M):
    p = int(str(N)[i])
    for smaller in range(2):
        lim = 10 if smaller else p+1
        for d in range(A):
            for x in range(lim):
                dp[i+1][smaller | (x < p)][(d+x) % A] += dp[i][smaller][d]
print(dp[M][0][0]+dp[M][1][0]-1)
