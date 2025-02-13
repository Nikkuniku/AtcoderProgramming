from collections import defaultdict

N = 1000000
S = 1
dp = defaultdict(lambda: -1)
dp[S] = 0
for v in range(1, N + 1):
    now = v
    cnt = 0
    while 1:
        if dp[now] != -1:
            dp[v] = dp[now] + cnt
            break
        if now % 2 == 0:
            now //= 2
            cnt += 1
        else:
            now = 3 * now + 1
            cnt += 1
p = max(dp.values())
ans = []
for k, v in dp.items():
    if v == p:
        ans.append(k)
print(p, ans)
