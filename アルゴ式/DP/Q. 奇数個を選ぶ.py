N, M = map(int, input().split())
W = list(map(int, input().split()))
dp = [[[False]*2 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0][0] = True
for i in range(N):
    for w in range(M+1):
        for k in range(2):
            dp[i+1][w][k] |= dp[i][w][k]
            if w-W[i] >= 0:
                dp[i+1][w][k ^ 1] |= dp[i][w-W[i]][k]
ans = 'No'
if dp[N][M][1]:
    ans = 'Yes'
print(ans)
