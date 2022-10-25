N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))

colors = [[0] for _ in range(256)]
for i in range(N):
    colors[C[i]].append(W[i])

dp = [[False]*(M+1) for _ in range(257)]
dp[0][0] = True
for i in range(256):
    cls = colors[i]
    for p in cls:
        for j in range(M+1):
            dp[i+1][j] |= dp[i][j]
            if j-p >= 0:
                dp[i+1][j] |= dp[i][j-p]

ans = 'No'
if dp[256][M]:
    ans = 'Yes'
print(ans)
