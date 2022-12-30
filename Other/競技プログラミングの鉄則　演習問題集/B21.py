N = int(input())
S = input()
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for L in range(1, N):
    for i in range(N-L):
        l = i
        r = i+L
        if S[l] == S[r]:
            if r-l > 1:
                dp[l][r] = dp[l+1][r-1]+2
            else:
                dp[l][r] = dp[l][l]+dp[r][r]
        else:
            if r-l > 1:
                dp[l][r] = max(dp[l+1][r], dp[l][r-1])
            else:
                dp[l][r] = dp[l][l]
print(dp[0][N-1])
