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
d = {0: 1, 1: 2, 2: 3, 3: 0, 4: 5, 5: 4, 6: 7, 7: 6}


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
            return 0
        i += di[d2]
        j += dj[d2]
        if (i < 0 or i >= 30 or j < 0 or j >= 30):
            return 0
        d = (d2 + 2) % 4
        length += 1
        if (i == si and j == sj and d == sd):
            return length


for i in range(30):
    for j in range(30):
        tmp = 0
        for k in range(4):
            p = loop_len(i, j, k)
            if tmp < p:
                tmp = p
        if tmp == 0:
            tmp2 = []
            for k in range(4):
                tiles[i][j] = d[tiles[i][j]]
                p = loop_len(i, j, k)
                tmp2.append(p)
            if max(tmp2) != 0:
                idx = tmp2.index(max(tmp2))
                ans[30*i + j] += idx+1
                for _ in range(idx+1):
                    tiles[i][j] = d[tiles[i][j]]

ans = list(map(str, ans))
print(''.join(ans))
