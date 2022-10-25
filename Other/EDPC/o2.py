n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0]*(1 << n)
dp[0] = 1
MOD = 1000000007
for s in range((1 << n)-1):
    i = bin(s).count("1")
    for j, v in enumerate(a[i]):
        if v == 0:
            continue
        if (s >> j) & 1 == 0:
            dp[s | (1 << j)] += dp[s]
            dp[s | (1 << j)] %= MOD
print(dp[(1 << n)-1])
