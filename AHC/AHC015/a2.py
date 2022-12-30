from collections import defaultdict
from random import randint, randrange
t = list(map(int, input().split()))
d = defaultdict(int)
d[1] = 'F'
d[2] = 'L'
d[3] = 'B'
LIM = 100
edge = 10
ans = []
box = [[-1]*edge for _ in range(edge)]

class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1]*(n + 1)
        self.size = [1]*(n + 1)

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        # 既に同じグループなら何もしない
        if x == y:
            return False

        # unionbysize
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.par[y] = x
        self.size[x] += self.size[y]

        return True

    def issize(self, x):
        return self.size[self.root(x)]


def tilt_box(pbox, direction):
    res_box = [[-1]*edge for _ in range(edge)]
    if direction == 'R':
        for i in range(edge):
            res_box[i] = sorted(pbox[i])
    elif direction == 'L':
        for i in range(edge):
            res_box[i] = sorted(pbox[i], reverse=True)
    elif direction == 'F':
        for j in range(edge):
            tmp = []
            for i in range(edge):
                tmp.append(pbox[i][j])
            tmp.sort(reverse=True)
            for i in range(edge):
                res_box[i][j] = tmp[i]
    else:
        for j in range(edge):
            tmp = []
            for i in range(edge):
                tmp.append(pbox[i][j])
            tmp.sort()
            for i in range(edge):
                res_box[i][j] = tmp[i]

    return res_box


def put_index(pbox, pt):
    blank = 0
    for i in range(edge):
        for j in range(edge):
            if pbox[i][j] == -1:
                blank += 1
            if blank == pt:
                return i, j


def existsametaste(pbox, x, y, taste):
    # Right
    for j in range(y+1, edge):
        if pbox[x][j] == taste:
            return 'R'
    # Left
    for j in range(y-1, -1, -1):
        if pbox[x][j] == taste:
            return 'L'
    # Front
    for i in range(x-1, -1, -1):
        if pbox[i][y] == taste:
            return 'F'
    # Back
    for i in range(x+1, edge):
        if pbox[i][y] == taste:
            return 'B'

    return False


def UnionFind_Score(tilted_box, direction):
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    uf = UnionFind(edge**2)
    for i in range(edge):
        for j in range(edge):
            for dx, dy in dxy:
                ni = i+dx
                nj = j+dy
                if 0 <= ni < edge and 0 <= nj < edge:
                    if tilted_box[i][j] == tilted_box[ni][nj]:
                        uf.unite(i*edge + j, ni*edge+j)
    # スコア評価
    tmp = 0
    for i in range(edge**2):
        if uf.root(i) == i:
            tmp += uf.issize(i)**2
    return (tmp, direction)


def maxdirection(pbox):
    res = []
    # Right
    tilted_box_R = tilt_box(pbox, 'R')
    res.append(UnionFind_Score(tilted_box_R, 'R'))
    # Left
    tilted_box_L = tilt_box(pbox, 'L')
    res.append(UnionFind_Score(tilted_box_L, 'L'))
    # Back
    tilted_box_B = tilt_box(pbox, 'B')
    res.append(UnionFind_Score(tilted_box_B, 'B'))
    # Front
    tilted_box_F = tilt_box(pbox, 'F')
    res.append(UnionFind_Score(tilted_box_F, 'F'))

    res.sort(key=lambda x: x[0])
    res = res[::-1]
    maxscore = res[0][0]

    resdire = []
    for s, d in res:
        if s == maxscore:
            resdire.append(d)
    return resdire[randrange(0, len(resdire))]


def distribution_candies(box, x, y, taste):
    # 右方向に貯まっているか
    res_right = 0
    for i in range(edge):
        for j in range(y+1, edge):
            if box[i][j] == taste:
                res_right += 1
    # 左方向に貯まっているか
    res_left = 0
    for i in range(edge):
        for j in range(y-1):
            if box[i][j] == taste:
                res_left += 1
    # 前方向に貯まっているか
    res_front = 0
    for i in range(x-1):
        for j in range(edge):
            if box[i][j] == taste:
                res_front += 1
    # 後方向に貯まっているか
    res_back = 0
    for i in range(x+1, edge):
        for j in range(edge):
            if box[i][j] == taste:
                res_back += 1
    res = []
    if res_right > 0:
        res.append((res_right, 'R'))
    if res_left > 0:
        res.append((res_left, 'L'))
    if res_front > 0:
        res.append((res_front, 'F'))
    if res_back > 0:
        res.append((res_back, 'B'))
    if res:
        return res[randrange(0, len(res))][1]
    else:
        return False


for i in range(LIM):
    p = int(input())
    x, y = put_index(box, p)
    taste = t[i]
    box[x][y] = taste
    res = existsametaste(box, x, y, taste)
    if not res:
        res = distribution_candies(box, x, y, taste)
    if not res:
        res = d[taste]
    print(res, flush=True)
    box = tilt_box(box, res)
    ans.append(res)


print('--')
print('--')
print('--')
print(*ans, sep="\n")
