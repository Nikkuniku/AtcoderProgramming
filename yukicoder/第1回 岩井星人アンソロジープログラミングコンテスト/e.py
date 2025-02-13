N, D, K = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
# dp[i+1][j][k]:i番目までで、j個選んだ時に、美しさの合計がkであるような満足度の最大値
dp0 = [[-(1 << 60)] * (K + 1) for _ in range(D + 1)]
dp1 = [[-(1 << 60)] * (K + 1) for _ in range(D + 1)]
dp0[0][0] = 0
for i in range(N):
    a, c = A[i], C[i]
    for j in range(D + 1):
        for k in range(K + 1):
            # 取らない
            dp1[j][k] = max(dp1[j][k], dp0[j][k])
            # 取る
            if j + 1 <= D:
                dp1[j + 1][min(k + c, K)] = max(
                    dp1[j + 1][min(k + c, K)], dp0[j][k] + a
                )
    dp0, dp1 = dp1, dp0
ans = dp0[D][K]
if sum(sorted(C, reverse=True)[:D]) < K:
    ans = "No"
print(ans)
