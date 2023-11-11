def alp2int(s):
    return ord(s) - 97


N = int(input())
S = input()
dp = [[[0] * 26 for _ in range(26)] for _ in range(N)]
MOD = 998244353
if S[0] != "?":
    s = alp2int(S[0])
    if S[1] != "?":
        dp[1][alp2int(S[1])][s] = 1
    else:
        for x in range(26):
            if x == s:
                continue
            dp[1][x][alp2int(S[0])] = 1
else:
    if S[1] != "?":
        t = alp2int(S[1])
        for x in range(26):
            if x == t:
                continue
            dp[1][t][x] = 1
    else:
        for x in range(26):
            for y in range(26):
                if x == y:
                    continue
                dp[1][x][y] = 1
for i in range(2, N):
    s = S[i]
    if s != "?":
        t = alp2int(S[i])
        for y in range(26):
            if y == t:
                continue
            for z in range(26):
                if z == y or z == t:
                    continue
                dp[i][t][y] += dp[i - 1][y][z]
                dp[i][t][y] %= MOD
    else:
        for x in range(26):
            for y in range(26):
                if y == x:
                    continue
                for z in range(26):
                    if z == x or z == y:
                        continue
                    dp[i][x][y] += dp[i - 1][y][z]
                    dp[i][x][y] %= MOD
ans = 0
if S[-1] != "?":
    if S[-2] != "?":
        ans = dp[N - 1][alp2int(S[-1])][alp2int(S[-2])]
    else:
        for y in range(26):
            if y == alp2int(S[-1]):
                continue
            ans += dp[N - 1][alp2int(S[-1])][y]
            ans %= MOD
else:
    if S[-2] != "?":
        for x in range(26):
            if x == alp2int(S[-2]):
                continue
            ans += dp[N - 1][x][alp2int(S[-2])]
            ans %= MOD
    else:
        for x in range(26):
            for y in range(26):
                if x == y:
                    continue
                ans += dp[N - 1][x][y]
                ans %= MOD
print(ans)
