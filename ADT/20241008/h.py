def calc_time(pi, pj, t):
    dist = ((pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2) ** 0.5
    return dist / t


def popcount(x):
    """xの立っているビット数をカウントする関数
    (xは64bit整数)"""

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007F


N, M = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N + M)]
INF = 1 << 60
dp = [[INF] * (N + M) for _ in range(1 << (N + M))]
for i in range(N + M):
    dp[1 << i][i] = calc_time([0, 0], P[i], 1)
K = ((1 << (N + M)) - 1) ^ ((1 << N) - 1)
for s in range(1 << (N + M)):
    # uから向かう
    for u in range(N + M):
        if not s & (1 << u):
            continue
        for v in range(N + M):
            if s & (1 << v):
                continue
            t = popcount(s & K)
            if dp[s | (1 << v)][v] > dp[s][u] + calc_time(P[u], P[v], 1 << t):
                dp[s | (1 << v)][v] = dp[s][u] + calc_time(P[u], P[v], 1 << t)
L = (1 << N) - 1
ans = 1 << 60
for s in range(1 << (N + M)):
    if s & L == L:
        for u in range(N + M):
            t = popcount(s & K)
            tmp = dp[s][u] + calc_time(P[u], [0, 0], 1 << t)
            ans = min(ans, tmp)
print(ans)
