from collections import defaultdict, deque


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


H, W, T = map(int, input().split())
A = [list(input()) for _ in range(H)]
cookie = 1
d = defaultdict(int)
CNT = 0
for i in range(H):
    CNT += A[i].count('o')
for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            d[(i, j)] = 0
        elif A[i][j] == 'G':
            d[(i, j)] = CNT+1
        elif A[i][j] == 'o':
            d[(i, j)] = cookie
            cookie += 1
cost = [[0]*(CNT+2) for _ in range(CNT+2)]


def BFS(x, y, num):
    q = deque([(x, y)])
    dist = [[-1]*W for _ in range(H)]
    dist[x][y] = 0
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    while q:
        vx, vy = q.popleft()
        for k in range(4):
            nx = vx+dx[k]
            ny = vy+dy[k]
            if 0 <= nx < H and 0 <= ny < W:
                if A[nx][ny] == '#' or dist[nx][ny] != -1:
                    continue
                dist[nx][ny] = dist[vx][vy]+1
                q.append((nx, ny))
    for i in range(H):
        for j in range(W):
            if A[i][j] == '#' or A[i][j] == '.':
                continue
            if A[i][j] == 'S':
                cost[num][0] = dist[i][j]
            elif A[i][j] == 'G':
                cost[num][CNT+1] = dist[i][j]
            elif A[i][j] == 'o':
                cost[num][d[(i, j)]] = dist[i][j]


for k, v in list(d.items()):
    BFS(k[0], k[1], v)
INF = 1 << 60
dp = [[INF]*CNT for _ in range(1 << CNT)]
for v in range(CNT):
    dp[1 << v][v] = cost[0][v+1]
for s in range(1, 1 << CNT):
    for v in range(CNT):
        for u in range(CNT):
            if dp[s][u] == INF:
                continue
            if (s >> v) & 1 == 0:
                dp[s | (1 << v)][v] = min(
                    dp[s | (1 << v)][v], dp[s][u]+cost[u+1][v+1])
ans = -1
if cost[0][CNT+1] <= T:
    ans = 0
for s in range(1, 1 << CNT):
    for v in range(CNT):
        if dp[s][v]+cost[v+1][CNT+1] <= T:
            ans = max(ans, popcount(s))
print(ans)
