def solve(N):
    dp = [[[0] * (1 << 3) for _ in range(2)] for _ in range(N + 1)]
    for x in range(1, 16):
        if x == 1:
            dp[1][x < 15][1 << 1] += 1
        elif x == 10:
            dp[1][x < 15][1 << 2] += 1
        else:
            dp[1][x < 15][0] += 1
    for i in range(1, N):
        for smaller in range(2):
            for s in range(1 << 3):
                for x in range(16):
                    if x == 0:
                        dp[i + 1][smaller | (x < 15)][s | (1 << 0)] += dp[i][smaller][s]
                    elif x == 1:
                        dp[i + 1][smaller | (x < 15)][s | (1 << 1)] += dp[i][smaller][s]
                    elif x == 10:
                        dp[i + 1][smaller | (x < 15)][s | (1 << 2)] += dp[i][smaller][s]
                    else:
                        dp[i + 1][smaller | (x < 15)][s] += dp[i][smaller][s]

    return dp[N][0][(1 << 3) - 1] + dp[N][1][(1 << 3) - 1]


ans = 0
for k in range(1, 16 + 1):
    print(k, solve(k))
    ans += solve(k)
print(ans)
print(hex(ans).upper())
