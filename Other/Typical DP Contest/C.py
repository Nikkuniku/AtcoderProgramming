def func(x, y):
    return 1 / (1 + pow(10, (y - x) / 400))


K = int(input())
R = [int(input()) for _ in range(1 << K)]
dp = [[0] * (1 << K) for _ in range(K + 1)]
isEnd = [[False] * (1 << K) for _ in range((1 << K))]
for i in range(1 << K):
    dp[0][i] = 1
for k in range(K):
    for i in range(1 << K):
        for j in range(1 << K):
            if j == i:
                continue
            if i // (1 << (k + 1)) == j // (1 << (k + 1)) and not isEnd[i][j]:
                dp[k + 1][i] += func(R[i], R[j]) * dp[k][i] * dp[k][j]
                isEnd[i][j] = True
print(*dp[K], sep="\n")
