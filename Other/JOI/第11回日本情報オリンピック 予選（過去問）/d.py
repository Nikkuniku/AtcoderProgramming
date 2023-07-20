from collections import defaultdict
n, k = map(int, input().split())
MOD = 10000
d = defaultdict(int)
for _ in range(k):
    a, b = map(int, input().split())
    d[a-1] = b

dp = [[[0]*4 for _ in range(4)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(n):
    m_range = [1, 2, 3] if d[i] == 0 else [d[i]]
    for j in range(4):
        for k in range(4):
            for m in m_range:
                if not (m == j and j == k):
                    dp[i+1][m][j] += dp[i][j][k]
                    dp[i+1][m][j] %= MOD
ans = 0
for i in range(4):
    for j in range(4):
        ans += dp[n][i][j]
ans %= MOD
print(ans)
