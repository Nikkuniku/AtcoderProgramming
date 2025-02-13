def check_palinrdome(s, t):
    p = list(s) + [t]
    return p == p[::-1]


from collections import defaultdict

N, K = map(int, input().split())
S = input()
MOD = 998244353
dp = [defaultdict(int) for _ in range(N + 1)]
dp[0][("")] = 1
for i in range(N):
    si = S[i]
    for t, v in dp[i].items():
        dt = list(t)
        if len(t) + 1 < K:
            if si == "?":
                for ti in ["A", "B"]:
                    dp[i + 1][tuple(dt + [ti])] += dp[i][t]
                    dp[i + 1][tuple(dt + [ti])] %= MOD
            else:
                next = tuple(dt + [si])
                dp[i + 1][next] += dp[i][t]
                dp[i + 1][next] %= MOD
        else:
            if si == "?":
                for ti in ["A", "B"]:
                    if check_palinrdome(dt, ti):
                        continue
                    dp[i + 1][tuple(dt[1:] + [ti])] += dp[i][t]
                    dp[i + 1][tuple(dt[1:] + [ti])] %= MOD
            else:
                if check_palinrdome(dt, si):
                    continue
                dp[i + 1][tuple(dt[1:] + [si])] += dp[i][t]
                dp[i + 1][tuple(dt[1:] + [si])] %= MOD
ans = 0
for v in dp[N].values():
    ans += v
    ans %= MOD
print(ans)
