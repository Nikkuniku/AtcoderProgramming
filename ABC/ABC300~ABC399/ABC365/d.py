N = int(input())
S = input()
dp = [[0, 0, 0] for _ in range(N + 1)]
for i in range(N):
    if S[i] == "P":
        dp[i + 1][0] = max(dp[i][1], dp[i][2])
        dp[i + 1][2] = max(dp[i][0], dp[i][1]) + 1
    elif S[i] == "R":
        dp[i + 1][0] = max(dp[i][1], dp[i][2]) + 1
        dp[i + 1][1] = max(dp[i][0], dp[i][2])
    elif S[i] == "S":
        dp[i + 1][1] = max(dp[i][0], dp[i][2]) + 1
        dp[i + 1][2] = max(dp[i][0], dp[i][1])
print(max(dp[N]))
