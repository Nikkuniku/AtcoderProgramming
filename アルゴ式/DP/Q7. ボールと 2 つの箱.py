N = int(input())
W = list(map(int, input().split()))
S = sum(W)
dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(S+1):
        dp[i+1][j] |= dp[i][j]
        if j-W[i] >= 0:
            dp[i+1][j] |= dp[i][j-W[i]]

ans = 1 << 18
for i in range(S+1):
    if dp[N][i]:
        ans = min(ans, abs(i - (S-i)))
print(ans)
