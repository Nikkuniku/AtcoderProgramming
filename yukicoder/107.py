n = int(input())
d = list(map(int, input().split()))
INF = 10**19
dp = [-INF]*(1 << n)
dp[0] = 100

for s in range(1 << n):
    if dp[s] <= 0:
        continue
    limit = 1
    # 今まで倒した悪い敵の数=ビットが1かつ値が負
    for j in range(n):
        if (s >> j) & 1 and d[j] < 0:
            limit += 1

    for v in range(n):
        # まだ戦っていない
        if (s >> v) & 1 == 0:
            # 正の値の時
            if d[v] >= 0:
                dp[s | (1 << v)] = min(
                    max(dp[s | (1 << v)], dp[s]+d[v]), limit*100)
            # 負の値の時
            elif dp[s]+d[v] > 0:
                dp[s | (1 << v)] = max(dp[s | (1 << v)], dp[s]+d[v])

ans = max(0, dp[(1 << n)-1])
print(ans)
