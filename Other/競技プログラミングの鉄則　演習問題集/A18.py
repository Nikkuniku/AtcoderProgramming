n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    for j in range(s+1):
        # その数を選ばない
        dp[i+1][j] |= dp[i][j]
        # その数が選べるならば選ぶ
        if j-a[i] >= 0:
            dp[i+1][j] |= dp[i][j-a[i]]

if dp[n][s]:
    print('Yes')
else:
    print('No')
