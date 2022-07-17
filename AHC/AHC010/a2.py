from collections import deque
import sys
to = [
    [1, 0, -1, -1],
    [3, -1, -1, 0],
    [-1, -1, 3, 2],
    [-1, 2, 1, -1],
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [2, -1, 0, -1],
    [-1, 3, -1, 1],
]
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
tiles = []
for _ in range(30):
    tiles.append(list(map(int, input())))
ans = [0]*900
dir = {0: 1, 1: 2, 2: 3, 3: 0, 4: 5, 5: 4, 6: 7, 7: 6}
sys.setrecursionlimit(10**6)

kouho = []


def loop_len(si, sj, sd):
    # (si, sj) のタイルに sd 方向のタイルから侵入した状態からスタートして環状線の長さを求める
    i = si
    j = sj
    d = sd
    re = 0
    length = 0
    while True:
        d2 = to[tiles[i][j]][d]
        if d2 == -1:
            kouho.append((i, j, d))
            return 0
        i += di[d2]
        j += dj[d2]
        if (i < 0 or i >= 30 or j < 0 or j >= 30):
            return 0
        d = (d2 + 2) % 4
        length += 1
        if (i == si and j == sj and d == sd):
            return length


flg = False


def bfs(i, j, d):
    cnt = 0
    q = deque([(i, j)])

    while q:

        if cnt > 100:
            return
        vx, vy = q.popleft()
        i = vx
        j = vy
        if (i < 0 or i >= 30 or j < 0 or j >= 30):
            return 0
        d2 = to[tiles[i][j]][d]
        if d2 == -1:
            tiles[i][j] = dir[tiles[i][j]]
            ans[30*i + j] += 1
            d2 = to[tiles[i][j]][d]
            if d2 == -1:
                tiles[i][j] = dir[tiles[i][j]]
                ans[30*i + j] += 1
                d2 = to[tiles[i][j]][d]
                if d2 == -1:
                    tiles[i][j] = dir[tiles[i][j]]
                    ans[30*i + j] += 1
                    d2 = to[tiles[i][j]][d]
                else:
                    i += di[d2]
                    j += dj[d2]
                    flg = True
            else:
                i += di[d2]
                j += dj[d2]
                flg = True

        else:
            i += di[d2]
            j += dj[d2]
            flg = True

        if flg:
            q.append((i, j))
            flg = False
        cnt += 1


for i in range(30):
    for j in range(30):
        for k in range(4):
            bfs(i, j, k)
            flg = False


for i in range(900):
    ans[i] %= 4
ans = list(map(str, ans))
print(''.join(ans))
