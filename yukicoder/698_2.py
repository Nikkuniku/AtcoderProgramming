n = int(input())
a = list(map(int, input().split()))
S = 1 << n

dp = [0]*S
for s in range(S):
    for u in range(n):
        if s >> u & 1:
            continue
        for v in range(u+1, n):
            if s >> v & 1:
                continue
            if dp[s | (1 << u) | (1 << v)] < dp[s]+(a[u] ^ a[v]):
                dp[s | (1 << u) | (1 << v)] = dp[s]+(a[u] ^ a[v])
print(dp[S-1])
