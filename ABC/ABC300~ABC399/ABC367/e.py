N, K = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
L = 61
dp = [[-1] * N for _ in range(L + 1)]
for i in range(N):
    dp[0][i] = X[i] - 1
for i in range(L):
    for v in range(N):
        dp[i + 1][v] = dp[i][dp[i][v]]
ans = [-1] * N
for v in range(N):
    to = v
    for j in range(L):
        if K & (1 << j):
            to = dp[j][to]
    ans[v] = A[to]
print(*ans)
