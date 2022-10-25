n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
can = []
for i in range(n):
    tmp = []
    for j, v in enumerate(a[i]):
        if v == 1:
            tmp.append(j)
    can.append(tmp)

dp = [[0]*(1 << n) for _ in range(n+1)]
dp[0][0] = 1
next = set([0])
MOD = 1000000007
for i in range(n):
    tmp = set()
    for s in next:
        for j in can[i]:
            if (s >> j) & 1 == 0:
                dp[i+1][s | (1 << j)] += dp[i][s]
                dp[i+1][s | (1 << j)] %= MOD
                tmp.add(s | (1 << j))
    next = tmp

print(dp[n][(1 << n)-1])
