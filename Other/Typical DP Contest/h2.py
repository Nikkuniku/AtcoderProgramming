from collections import defaultdict

N, W, C = map(int, input().split())
goods = defaultdict(list)
for _ in range(N):
    w, v, c = map(int, input().split())
    goods[c].append((w, v))
INF = 1e18
dp = [[-INF] * (W + 1) for _ in range(C + 1)]
dp[0][0] = 0
Colors = list(goods.keys())
for i, c in enumerate(Colors):
    for k in range(C, 0, -1):
        ep = [-INF] * (W + 1)
        ep[0] = 0
        for w, v in goods[c]:
            for j in range(W, -1, -1):
                # 取る場合
                if j - w >= 0:
                    ep[j] = max(ep[j], dp[k - 1][j - w] + v)
                    ep[j] = max(ep[j], ep[j - w] + v)
        for j in range(W + 1):
            dp[k][j] = max(dp[k][j], ep[j])
ans = max(dp[C])
print(ans)
