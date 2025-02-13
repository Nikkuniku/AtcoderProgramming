f = open("./0081_matrix.txt", "r")
S = [s.split(",") for s in f.read().split("\n")]
N = 80
for i in range(N):
    for j in range(N):
        S[i][j] = int(S[i][j])
INF = 1 << 60
dp = [[INF] * (N + 1) for _ in range(N + 1)]
dp[1][1] = S[0][0]
for i in range(N):
    for j in range(N):
        if i == j == 0:
            continue
        dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) + S[i][j]
print(S)
print(dp[N][N])
