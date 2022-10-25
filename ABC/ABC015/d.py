W = int(input())
N, K = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0]*(W+1) for _ in range(K+1)]
for i in range(N):
    a, b = ab[i]
    for k in range(K, -1, -1):
        for w in range(W, -1, -1):
            if k-1 >= 0 and w-a >= 0:
                dp[k][w] = max(dp[k][w], dp[k-1][w-a]+b)

print(max(dp[K]))
