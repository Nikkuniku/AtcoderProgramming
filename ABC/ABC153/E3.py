H, N = map(int, input().split())
magic = [tuple(map(int, input().split())) for _ in range(N)]
INF = 1000_000_000_000_000
dp = [INF]*(H+1)
dp[0] = 0

for h in range(H+1):
    for a, b in magic:
        dp[min(h+a, H)] = min(dp[min(h+a, H)], dp[h]+b)
print(dp[H])
