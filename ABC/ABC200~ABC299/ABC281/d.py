N, K, D = map(int, input().split())
A = list(map(int, input().split()))
dp = [[[-1]*D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(K+1):
        for d in range(D):
            # aiを選ばない
            if dp[i][j][d] != -1:
                dp[i+1][j][d] = max(dp[i+1][j][d], dp[i][j][d])
            # aiを選ぶ
            if j-1 >= 0 and dp[i][j-1][(d-A[i]) % D] != -1:
                dp[i+1][j][d] = max(dp[i+1][j][d], dp[i]
                                    [j-1][(d-A[i]) % D]+A[i])
print(dp[N][K][0])
