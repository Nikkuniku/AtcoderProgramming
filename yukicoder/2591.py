N = int(input())
S = input()
A = list(map(int, input().split()))
INF = 1 << 60
dp = [[INF] * (2 * N) for _ in range(2 * N + 1)]
dp[0][0] = 0
for i in range(2 * N):
    for j in range(2 * N):
        if j - 1 >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - 1] + A[i] * (S[i] == ")"))
        if j + 1 < 2 * N:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j + 1] + A[i] * (S[i] == "("))
ans = dp[2 * N][0]
print(ans)
