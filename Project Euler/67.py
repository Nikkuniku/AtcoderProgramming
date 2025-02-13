f = open("./0067_triangle.txt", "r")
S = [list(map(int, s.split())) for s in f.read().split("\n")]
N = len(S)
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    if i == 0:
        dp[i + 1][0] = S[i][0]
    else:
        for j in range(len(S[i])):
            if j < len(S[i - 1]):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + S[i][j])
            if j - 1 < len(S[i - 1]):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - 1] + S[i][j])
ans = max(dp[N - 1])
print(dp[N - 1])
print(ans)
