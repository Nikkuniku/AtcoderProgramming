n = int(input())
s = input()
d = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9
}
S = 1 << 10
dp = [[[0]*10 for _ in range(S)] for _ in range(n+1)]

for i in range(n):
    p = s[i]
    for q in range(S):
        for u in range(10):
            if not (q >> u) & 1:
                continue
            if u == d[p]:
                dp[i+1][q][u] += dp[i][q][u]+1
            else:
                for v in range(10):
                    if (q >> v) & 1:
                        continue
                    dp[i+1][q | (1 << v)][v] += dp[i][q][u]
print(dp[n][S-1])
