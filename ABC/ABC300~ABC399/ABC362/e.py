from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
dp = [[defaultdict(int) for _ in range(N)] for _ in range(N + 1)]
ans = [0] * (N + 1)
for k in range(1, N):
    if k == 1:
        for i in range(N):
            for j in range(i):
                d = A[i] - A[j]
                dp[k + 1][i][d] += 1
                dp[k + 1][i][d] %= MOD
    else:
        for i in range(N):
            for j in range(i):
                d = A[i] - A[j]
                if dp[k][j][d] > 0:
                    dp[k + 1][i][d] += dp[k][j][d]
                    dp[k + 1][i][d] %= MOD
for k in range(2, N + 1):
    for i in range(N):
        for _, v in dp[k][i].items():
            if v > 0:
                ans[k] += v
                ans[k] %= MOD
ans[1] = N % MOD
print(*ans[1:])
