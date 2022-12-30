n = int(input())
dp = [[[[0, 0, 0, 0] for _ in range(4)]for _ in range(4)] for _ in range(n+1)]
d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
dp[0][3][3][3] = 1

MOD = 1000_000_007
for i in range(n):
    for s in ['A', 'G', 'C', 'T']:
        for t in ['A', 'G', 'C', 'T']:
            for k in ['A', 'G', 'C', 'T']:
                for m in ['A', 'G', 'C', 'T']:
                    if t == 'A' and k == 'G' and m == 'C':
                        continue
                    elif t == 'A' and k == 'C' and m == 'G':
                        continue
                    elif t == 'G' and k == 'A' and m == 'C':
                        continue
                    elif s == 'A' and t == 'G' and m == 'C':
                        continue
                    elif s == 'A' and k == 'G' and m == 'C':
                        continue
                    dp[i+1][d[t]][d[k]][d[m]] += dp[i][d[s]][d[t]][d[k]]
                    dp[i+1][d[t]][d[k]][d[m]] %= MOD

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[n][i][j][k]
            ans %= MOD
print(ans)
