def digitsquare(k):
    res = 0
    while k > 0:
        res += pow(k % 10, 2)
        k //= 10
    return res


N = 10000000
dp = [-1] * (N + 1)
for i in range(1, N + 1):
    if dp[i] != -1:
        continue
    seen = set([i])
    now = i
    endval = -1
    while 1:
        now = digitsquare(now)
        seen.add(now)
        if now == 1 or now == 89:
            endval = now
            break
        elif dp[now] != -1:
            endval = dp[now]
            break
    for s in seen:
        dp[s] = endval
ans = 0
for i in range(N + 1):
    ans += dp[i] == 89
print(ans)
