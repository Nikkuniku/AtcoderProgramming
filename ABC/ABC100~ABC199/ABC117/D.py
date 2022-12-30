N, K = map(int, input().split())
a = list(map(int, input().split()))
INF = float('inf')
dp = [[-INF, -INF] for _ in range(43)]
dp[42][0] = 0
for i in range(41, -1, -1):
    d = pow(2, i)
    cnt_1 = 0
    for ai in a:
        cnt_1 += (ai >> i) & 1
    cnt_0 = N-cnt_1

    if (K >> i) & 1:
        dp[i][0] = dp[i+1][0] + cnt_0*d
        dp[i][1] = max(dp[i][1], dp[i+1][0]+cnt_1*d)
        dp[i][1] = max(dp[i][1], dp[i+1][1]+cnt_0*d)
    else:
        dp[i][0] = dp[i+1][0] + cnt_1*d
        dp[i][1] = max(dp[i][1], dp[i+1][1]+cnt_0*d)

    dp[i][1] = max(dp[i][1], dp[i+1][1]+cnt_1*d)

print(max(dp[0]))
