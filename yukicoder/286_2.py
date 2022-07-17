n = int(input())
goods = []
for _ in range(n):
    goods.append(int(input()))
S = 1 << n
INF = 10**18
dp = [INF]*S
dp[0] = 0

for s in range(S):
    for v in range(n):
        if s >> v & 1:
            continue
        discount = 0
        for u in range(n):
            if s >> u & 1:
                discount += goods[u]
        sales = max(goods[v]-discount % 1000, 0)
        if dp[s | (1 << v)] > dp[s]+sales:
            dp[s | (1 << v)] = dp[s]+sales
print(dp[S-1])
