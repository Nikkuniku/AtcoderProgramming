N, X = map(int, input().split())
P = list(map(int, input().split()))
R = [[0] * (N + 1) for _ in range(N + 1)]
R[0][0] = 1
for i in range(N):
    p = P[i] / 100
    for j in range(N + 1):
        # 当たる
        if j - 1 >= 0:
            R[i + 1][j] += R[i][j - 1] * p
        # 当たらない
        R[i + 1][j] += R[i][j] * (1 - p)
dp = [0] * (X + 1)
dp[X] = 0
for x in range(X - 1, -1, -1):
    temp = R[N][0]
    for y in range(1, N + 1):
        if x + y <= X:
            temp += dp[x + y] * R[N][y]
        temp += R[N][y]
    dp[x] = temp / (1 - R[N][0])
print(dp[0])
