N = int(input())
P = list(map(int, input().split()))
S = input()
spoon_L = [False] * N
spoon_R = [False] * N
ans = 0
MOD = 998244353
dp = [[0, 0] for _ in range(N + 1)]
dp[0] = [1, 1]
for i in range(N):
    p = P[i] - 1
    s = S[p]
    l, r = p, p + 1
    if p == N - 1:
        r = 0
    # 左を取る
    if spoon_L[r]:
        spoon_L[l] = True
        if s in ("L", "R"):
            dp[i + 1][0] = dp[i][0]
        elif s == "?":
            dp[i + 1][0] = 2 * dp[i][0]
    else:
        if s in ("L", "?"):
            spoon_L[l] = True
            dp[i + 1][0] = dp[i][0]

    # 右を取る
    if spoon_R[l]:
        spoon_R[r] = True
        if s in ("L", "R"):
            dp[i + 1][1] = dp[i][1]
        elif s == "?":
            dp[i + 1][1] = 2 * dp[i][1]
    else:
        if s in ("R", "?"):
            spoon_R[r] = True
            dp[i + 1][1] = dp[i][1]
    dp[i + 1][0] %= MOD
    dp[i + 1][1] %= MOD
ans = sum(dp[N]) % MOD
print(ans)
