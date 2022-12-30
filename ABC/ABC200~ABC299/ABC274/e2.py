N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
booster = [list(map(int, input().split())) for _ in range(M)]
points = booster+town
V = len(points)
INF = float('inf')
dp = [[INF]*V for _ in range(1 << V)]
sx, sy = 0, 0
for v in range(V):
    gx, gy = points[v]
    dist = ((sx-gx)**2 + (sy-gy)**2)**(1/2)
    dp[1 << v][v] = dist
for s in range(1 << V):
    speed = 1
    for i in range(M):
        if s & (1 << i):
            speed *= 2
    for u in range(V):
        if not s & (1 << u) and s != 0:
            continue
        sx, sy = points[u]
        for v in range(V):
            if s & (1 << v):
                continue
            gx, gy = points[v]
            dist = ((sx-gx)**2 + (sy-gy)**2)**(1/2)
            if dp[s | (1 << v)][v] > dp[s][u]+dist/speed:
                dp[s | (1 << v)][v] = dp[s][u]+dist/speed
p = (((1 << N)-1) << M)
ans = INF


def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007f


for i in range(1 << M):
    q = p | i
    speed = pow(2, popcount(i))
    for v in range(N+M):
        if not q & (1 << v):
            continue
        sx, sy = points[v]
        gx, gy = 0, 0
        dist = ((sx-gx)**2 + (sy-gy)**2)**(1/2)
        ans = min(ans, dp[q][v]+dist/speed)
print(ans)
