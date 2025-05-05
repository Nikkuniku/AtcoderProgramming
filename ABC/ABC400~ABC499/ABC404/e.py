N = int(input())
C = [0] + list(map(int, input().split()))
A = [0] + list(map(int, input().split()))
INF = 1 << 60
dp = [INF] * N
dp[0] = 0
fr = [-1] * N
for i in range(1, N):
    for j in range(1, C[i] + 1):
        if i - j < 0:
            continue
        if A[i - j] > 0:
            dp[i] = min(dp[i], dp[i - j])
        else:
            dp[i] = min(dp[i], dp[i - j] + 1)
        fr[i] = fr[i - j]
print(dp)
ans = 0
for i in range(N):
    if A[i] > 0:
        ans += dp[i]
print(ans)
