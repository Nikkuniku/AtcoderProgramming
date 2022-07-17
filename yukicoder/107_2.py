n = int(input())
d = list(map(int, input().split()))
S = 1 << n
dp = [0]*S
dp[0] = 100
for s in range(S):
    if dp[s] == 0:
        continue
    for v in range(n):
        if s & (1 << v):
            continue
        cnt = 0
        for u in range(n):
            if u == v:
                continue
            if s & (1 << u) and d[u] < 0:
                cnt += 1
        hp = min(dp[s]+d[v], 100*(1+cnt))
        if dp[s | (1 << v)] < hp:
            dp[s | (1 << v)] = hp
print(dp[S-1])
