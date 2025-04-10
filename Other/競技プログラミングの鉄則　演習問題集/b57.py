N, K = map(int, input().split())
L = 30
# dp[m][n]:nから2^m回移動したときの値
dp = [[-1] * (N + 1) for _ in range(L + 1)]
for i in range(N + 1):
    k = i
    next = i
    while k > 0:
        next -= k % 10
        k //= 10
    dp[0][i] = next
for i in range(L):
    for j in range(N + 1):
        dp[i + 1][j] = dp[i][dp[i][j]]
ans = [-1] * (N + 1)
for n in range(N + 1):
    now = n
    for j in range(30):
        if K & (1 << j):
            now = dp[j][now]
    ans[n] = now
print(*ans[1:], sep="\n")
