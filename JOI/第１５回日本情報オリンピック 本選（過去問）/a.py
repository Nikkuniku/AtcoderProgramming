N, M, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
INF = 1 << 60
# dp[i+1]:オレンジiまでを箱に詰めた時のコスト最小値
dp = [0]
for i in range(N):
    MaxW = 0
    MinW = INF
    tmp = INF
    for j in range(M):
        if i-j < 0:
            break
        MaxW = max(MaxW, A[i-j])
        MinW = min(MinW, A[i-j])
        tmp = min(tmp, K+dp[i+1-j-1]+(MaxW-MinW)*(j+1))
    dp.append(tmp)
print(dp[N])
