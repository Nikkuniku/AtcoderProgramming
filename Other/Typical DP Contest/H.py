N, W, C = map(int, input().split())
goods = [[] for _ in range(50)]
good = []

for _ in range(N):
    w, v, c = map(int, input().split())
    goods[c-1].append((w, v))
for c in goods:
    if c:
        good.append(c)

dp = [[0]*(W+1) for _ in range(len(good)+1)]
for i in range(len(good)):
    for w, v in good[i]:
        for c in range(i, -1, -1):
            for j in range(W+1):
                dp[c+1][j] = max(dp[c+1][j], dp[c][j])
                if j-w >= 0:
                    dp[c+1][j] = max(dp[c+1][j], dp[c][j-w]+v)

print(dp[C][W])
