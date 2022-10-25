n = int(input())
dp = [[[[[0]*4 for _ in range(4)] for _ in range(4)]
       for _ in range(2)] for _ in range(n+1)]

d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
# 初期化
for i in ['A', 'G', 'C', 'T']:
    for j in ['A', 'G', 'C', 'T']:
        for k in ['A', 'G', 'C', 'T']:
            dp[3][0][d[i]][d[j]][d[k]] = 1
dp[3][0][d['A']][d['G']][d['C']] = 0
dp[3][0][d['A']][d['C']][d['G']] = 0
dp[3][0][d['G']][d['A']][d['C']] = 0
dp[3][1][d['A']][d['G']][d['C']] = 1
dp[3][1][d['A']][d['C']][d['G']] = 1
dp[3][1][d['G']][d['A']][d['C']] = 1

MOD = 1000_000_007
for i in range(4, n+1):
    for s in ['A', 'G', 'C', 'T']:
        for t in ['A', 'G', 'C', 'T']:
            for k in ['A', 'G', 'C', 'T']:
                for m in ['A', 'G', 'C', 'T']:
                    dp[i][0][d[t]][d[k]][d[m]] += dp[i-1][0][d[s]][d[t]][d[k]]
                    dp[i][1][d[t]][d[k]][d[m]] += dp[i-1][1][d[s]][d[t]][d[k]]
                    if t == 'A' and k == 'G' and m == 'C':
                        dp[i][1][d[t]][d[k]][d[m]] += dp[i-1][0][d[s]][d[t]][d[k]]
                    elif s != 'A' and t == 'G' and k == 'A' and m == 'C':
                        dp[i][1][d[t]][d[k]][d[m]] += dp[i-1][0][d[s]][d[t]][d[k]]
                    elif t == 'A' and k == 'C' and m == 'G':
                        dp[i][1][d[t]][d[k]][d[m]] += dp[i-1][0][d[s]][d[t]][d[k]]
                    elif s == 'A' and t != 'A' and k == 'G' and m == 'C':
                        dp[i][1][d[t]][d[k]][d[m]] += dp[i-1][0][d[s]][d[t]][d[k]]
                    elif s == 'A' and t == 'G' and k != 'C' and m == 'C':
                        dp[i][1][d[t]][d[k]][d[m]] += dp[i-1][0][d[s]][d[t]][d[k]]

                    dp[i][0][d[t]][d[k]][d[m]] %= MOD
                    dp[i][1][d[t]][d[k]][d[m]] %= MOD
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[n][1][i][j][k]
            ans %= MOD
ans = (pow(4, n, MOD)-ans) % MOD
print(ans)
