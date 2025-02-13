N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [False] * (N + 1)
for x in range(N + 1):
    for a in A:
        if x - a >= 0:
            dp[x] |= not dp[x - a]
ans = "First" if dp[N] else "Second"
print(ans)
