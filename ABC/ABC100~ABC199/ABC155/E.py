N = '0'+input()
M = len(N)
INF = 1 << 60
dp = [[INF]*2 for _ in range(M+1)]
dp[M-1] = [0, 0]
for i in range(M-1, -1, -1):
    p = int(N[i])
    for smaller in range(2):
        if smaller:
            for x in range(10):
                if p <= x-1 <= 9:
                    dp[i-1][smaller | (x-1 < p)] = min(dp[i-1]
                                                       [smaller | (x-1 < p)], dp[i][smaller]+x+x-1-p)
                else:
                    dp[i-1][smaller | (x-1 < p)] = min(dp[i-1]
                                                       [smaller | (x-1 < p)], dp[i][smaller]+x+10+x-1-p)
        else:
            for x in range(10):
                dp[i-1][smaller | (x < p)] = min(dp[i-1]
                                                 [smaller], dp[i][smaller] + x+x-p)
print(dp)
