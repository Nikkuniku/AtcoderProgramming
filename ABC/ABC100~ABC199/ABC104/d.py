S = input()
N = len(S)
MOD = 10**9 + 7
dp = [[[0] * 3 for _ in range(3)] for _ in range(N + 1)]
d = {"A": 0, "B": 1, "C": 2}
if S[0] == "A" or S[0] == "?":
    dp[1][0][0] = 1
for i in range(1, N):
    if S[i] == "?":
        for j in range(3):
            for k in range(3):
                for m in range(3):
                    dp[i + 1][j][k] += dp[i][m][k]
    else:
        j = d[S[i]]
        for k in range(3):
            for m in range(3):
                dp[i + 1][j][k] += dp[i][m][k]

    if S[i] in ("A", "?"):
        for j in range(3):
            dp[i + 1][0][0] += dp[i][j][0] > 0
    if S[i] in ("B", "?"):
        for j in range(3):
            dp[i + 1][1][1] += dp[i][j][0]
    if S[i] in ("C", "?"):
        for j in range(3):
            dp[i + 1][2][2] += dp[i][j][1]
print(*dp, sep="\n")
ans = 0
if S[-1] == "?":
    for j in range(3):
        ans += dp[N][j][2]
else:
    ans = dp[N][d[S[-1]]][2] % MOD
print(ans)
