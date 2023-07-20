from collections import defaultdict, deque


def decide(lim):
    # 各数字の高さの決定
    i = 0
    j = 1
    high = defaultdict(int)
    h = 0
    cnt = 0
    while i <= lim:
        high[i] = h
        i += 1
        cnt += 1
        if cnt == j:
            cnt = 0
            j += 1
            h += 1
    return high


M = 30
N = M*(M+1)//2
B = [list(map(int, input().split()))+[-1]*(M-1-i) for i in range(M)]
d = defaultdict(lambda: -1)
ball = defaultdict(lambda: -1)
for i in range(M):
    for j in range(M):
        if B[i][j] == -1:
            continue
        d[B[i][j]] = (i, j)
        ball[(i, j)] = B[i][j]
zahyo = set()
for i in range(M):
    for j in range(i+1):
        zahyo.add((i, j))
height = decide(N)
tier_list = defaultdict(list)
for v in range(N):
    tier_list[height[v]].append(v)
dxy = [(-1, -1),  (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
ans = []
kakutei = set()
for v in range(N):
    # ボールvを適切な高さへ移動させる
    sx, sy = d[v]
    # その高さに既にいるのならば端っこに寄せる
    if sx == height[v]:
        left = 0
        right = 0
        # 左側・右側の空きボールを数える
        for j in range(sx+1):
            if height[ball[(sx, j)]] != sx:
                if j < sy:
                    left += 1
                elif sy < j:
                    right += 1
        ope_tmp = []
        if left > 0 and right == 0:
            for j in range(sy, -1, -1):
                if height[ball[(sx, j)]] != sx:
                    py = j
                    break
            for pj in range(sy, py, -1):
                ope_tmp.append([sx, pj, sx, pj-1])
        elif left == 0 and right > 0:
            for j in range(sy+1, sx+1):
                if height[ball[(sx, j)]] != sx:
                    py = j
                    break
            for pj in range(sy+1, py):
                ope_tmp.append([sx, pj, sx, pj+1])
        elif left > 0 and right > 0:
            if left >= right:
                for j in range(sy, -1, -1):
                    if height[ball[(sx, j)]] != sx:
                        py = j
                        break
                for pj in range(sy, py, -1):
                    ope_tmp.append([sx, pj, sx, pj-1])
            else:
                for j in range(sy+1, sx+1):
                    if height[ball[(sx, j)]] != sx:
                        py = j
                        break
                for pj in range(sy+1, py):
                    ope_tmp.append([sx, pj, sx, pj+1])
        if ope_tmp:
            for c in ope_tmp:
                ans.append(c)
                vx, vy, nx, ny = c
                d[ball[(vx, vy)]], d[ball[(nx, ny)]] = (nx, ny), (vx, vy)
                ball[(vx, vy)], ball[(nx, ny)] = ball[(nx, ny)], ball[(vx, vy)]
        kakutei.add(v)
        continue
    q = deque([(sx, sy)])
    dist = defaultdict(lambda: -1)
    dist[(sx, sy)] = 0
    root = defaultdict(list)
    # 既に確定したボールは通らないようにする
    for w in kakutei:
        dist[d[w]] = 0
    # このボールが進む高さであって、まだ確定していない点
    kouho = []
    for j in range(height[v]+1):
        if dist[(height[v], j)] == -1:
            kouho.append((height[v], j))
    while q:
        vx, vy = q.popleft()
        for dx, dy in dxy:
            nx, ny = vx+dx, vy+dy
            if (nx, ny) not in zahyo:
                continue
            if dist[(nx, ny)] == -1:
                dist[(nx, ny)] = dist[(vx, vy)]+1
                q.append((nx, ny))
                root[(nx, ny)] = (vx, vy)
    # 最短距離を採用する
    kyori = []
    for i, j in kouho:
        if dist[(i, j)] == -1:
            continue
        kyori.append((dist[(i, j)], i, j))
    kyori.sort()
    operation = []
    if kyori:
        nowx, nowy = kyori[0][1], kyori[0][2]
        while nowx != sx or nowy != sy:
            prex, prey = root[(nowx, nowy)]
            operation.append([prex, prey, nowx, nowy])
            nowx, nowy = prex, prey
    operation = operation[::-1]
    for c in operation:
        ans.append(c)
        vx, vy, nx, ny = c
        d[ball[(vx, vy)]], d[ball[(nx, ny)]] = (nx, ny), (vx, vy)
        ball[(vx, vy)], ball[(nx, ny)] = ball[(nx, ny)], ball[(vx, vy)]
    kakutei.add(v)

with open('test.txt', 'w', encoding='utf-8') as file:
    file.write(str(min(len(ans), 10000))+"\n")
    for i in range(min(len(ans), 10000)):
        tmp = [str(c) for c in ans[i]]
        file.write(' '.join(tmp)+"\n")
print(len(ans))
for c in ans:
    print(*c)
