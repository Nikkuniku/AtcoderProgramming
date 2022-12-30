def cost(s):
    res = 1
    if s == '-':
        res *= -1
    return res


H, W = map(int, input().split())
masu = [list(input()) for _ in range(H)]
dp = [[0]*W for _ in range(H)]
if H > 1 or W > 1:
    dp[H-1][W-1] = 0
if H > 1:
    j = W-1
    for i in range(H-2, -1, -1):
        if (i+j) % 2 == 0:
            dp[i][j] = dp[i+1][j]+cost(masu[i+1][j])
        else:
            dp[i][j] = dp[i+1][j]-cost(masu[i+1][j])

if W > 1:
    i = H-1
    for j in range(W-2, -1, -1):
        if (i+j) % 2 == 0:
            dp[i][j] = dp[i][j+1]+cost(masu[i][j+1])
        else:
            dp[i][j] = dp[i][j+1]-cost(masu[i][j+1])


if H > 1 and W > 1:
    for i in range(H-2, -1, -1):
        for j in range(W-2, -1, -1):
            if (i+j) % 2 == 0:
                dp[i][j] = max(dp[i+1][j]+cost(masu[i+1][j]),
                               dp[i][j+1]+cost(masu[i][j+1]))
            else:
                dp[i][j] = min(dp[i+1][j]-cost(masu[i+1][j]),
                               dp[i][j+1]-cost(masu[i][j+1]))


if dp[0][0] == 0:
    ans = 'Draw'
elif dp[0][0] < 0:
    ans = 'Aoki'
else:
    ans = 'Takahashi'
print(ans)
