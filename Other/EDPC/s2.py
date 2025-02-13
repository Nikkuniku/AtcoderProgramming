K = input()
D = int(input())
N = len(K)
MOD = 1000000007
# dp[i+1][smaller][m]:左からi番目まで見た時に、smallerであってDで割った余りがmであるような数の個数
dp0 = [[0] * D for _ in range(2)]
dp1 = [[0] * D for _ in range(2)]
# 初期値
dp0[0][0] = 1
for i in range(N):
    p = int(K[i])
    for smaller in range(2):
        Limit = 10 if smaller == 1 else p + 1
        for m in range(D):
            for x in range(Limit):
                dp1[smaller | (x < p)][(m + x) % D] += dp0[smaller][m]
                dp1[smaller | (x < p)][(m + x) % D] %= MOD
    dp0, dp1 = dp1, [[0] * D for _ in range(2)]
# 0が答えに含まれてしまうので除く
ans = (dp0[0][0] + dp0[1][0] - 1) % MOD
print(ans)
