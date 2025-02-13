N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [(A[i], B[i]) for i in range(N)]
C.sort()
M = max(A)
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1
MOD = 998244353
for i in range(N):
    for s in range(M + 1):
        dp[i + 1][s] += dp[i][s]
        if s - C[i][1] >= 0:
            dp[i + 1][s] += dp[i][s - C[i][1]]
        dp[i + 1][s] %= MOD
ans = 0
for i in range(N):
    if C[i][0] < C[i][1]:
        continue
    K = C[i][0] - C[i][1]
    for p in range(K + 1):
        ans += dp[i][p]
        ans %= MOD
print(ans)
