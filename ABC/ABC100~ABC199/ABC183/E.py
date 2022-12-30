H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dp = [[0]*W for _ in range(H)]
Vertical = [[0]*W for _ in range(H)]
Horizontal = [[0]*W for _ in range(H)]
Diagonal = [[0]*W for _ in range(H)]
dp[0][0] = 1
Vertical[0][0] = 1
Horizontal[0][0] = 1
Diagonal[0][0] = 1
MOD = 10**9 + 7
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        if S[i][j] == '#':
            continue
        if j-1 >= 0:
            dp[i][j] += Horizontal[i][j-1]
        if i-1 >= 0:
            dp[i][j] += Vertical[i-1][j]
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] += Diagonal[i-1][j-1]

        if j-1 >= 0:
            Horizontal[i][j] = Horizontal[i][j-1]+dp[i][j]
        else:
            Horizontal[i][j] = dp[i][j]
        if i-1 >= 0:
            Vertical[i][j] = Vertical[i-1][j]+dp[i][j]
        else:
            Vertical[i][j] = dp[i][j]
        if i-1 >= 0 and j-1 >= 0:
            Diagonal[i][j] = Diagonal[i-1][j-1]+dp[i][j]
        else:
            Diagonal[i][j] = dp[i][j]

        dp[i][j] %= MOD
        Horizontal[i][j] %= MOD
        Vertical[i][j] %= MOD
        Diagonal[i][j] %= MOD


ans = dp[H-1][W-1]
print(ans)
