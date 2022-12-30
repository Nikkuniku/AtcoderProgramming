a, b = map(int, input().split())


def solve(n):
    m = len(str(n))
    dp = [[[[0, 0] for _ in range(2)] for _ in range(2)] for _ in range(m+1)]
    dp[0][0][0][0] = 1

    for i in range(m):
        for smaller in range(2):
            limit = 10 if smaller else int(str(n)[i])+1
            for j in range(2):
                for k in range(2):
                    for x in range(limit):
                        dp[i+1][smaller | (x < int(str(n)[i]))][j | (x == 4)
                                                                ][k | (x == 9)] += dp[i][smaller][j][k]

    ans = dp[m][0][1][0]+dp[m][0][0][1]+dp[m][0][1][1] + \
        dp[m][1][1][0]+dp[m][1][0][1]+dp[m][1][1][1]
    return ans


ans = solve(b)-solve(a-1)
print(ans)
