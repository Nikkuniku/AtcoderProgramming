N, X = map(int, input().split())
A = list(map(int, input().split()))


def solve(N, X, k, A):
    # dp[i][j][k]:i番目まで見た時に選んだ個数がj個で和の余りがkである物の最大値
    # X-k*pがkの倍数である。
    # X-dp[i][j][k]≡0 mod k　でないとダメ
    INF = 1 << 60
    dp = [[[-INF] * k for _ in range(k + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(k + 1):
            for m in range(k):
                if dp[i][j][m] == -INF:
                    continue
                # 選ぶ
                if j + 1 <= k:
                    dp[i + 1][j + 1][(m + A[i]) % k] = max(
                        dp[i + 1][j + 1][(m + A[i]) % k], dp[i][j][m] + A[i]
                    )
                # 選ばない
                dp[i + 1][j][m] = max(dp[i + 1][j][m], dp[i][j][m])
    return dp[N][k][X % k]


ans = 1 << 60
for k in range(1, N + 1):
    res = solve(N, X, k, A)
    if res == -(1 << 60):
        continue
    temp = (X - res) // k
    ans = min(ans, temp)
print(ans)
