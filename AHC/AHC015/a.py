from collections import defaultdict
from random import randrange

t = list(map(int, input().split()))
d = defaultdict(int)
d[1] = 'F'
d[2] = 'B'
d[3] = 'L'
LIM = 100
edge = 10
ans = []
box = [[-1]*edge for _ in range(edge)]


def tilt_box(box, direction):
    if direction == 'R':
        for i in range(len(box)):
            box[i] = sorted(box[i])
    elif direction == 'L':
        for i in range(len(box)):
            box[i] = sorted(box[i], reverse=True)
    elif direction == 'F':
        for j in range(len(box)):
            tmp = []
            for i in range(len(box)):
                tmp.append(box[i][j])
            tmp.sort()
            for i in range(len(box)):
                box[i][j] = tmp[i]
    else:
        for j in range(len(box)):
            tmp = []
            for i in range(len(box)):
                tmp.append(box[i][j])
            tmp.sort(reverse=True)
            for i in range(len(box)):
                box[i][j] = tmp[i]


def put_index(box, pt):
    blank = 0
    for i in range(len(box)):
        for j in range(len(box)):
            if box[i][j] == -1:
                blank += 1
            if blank == pt:
                return i, j


def existsametaste(box, x, y, taste):
    # Right
    res = []
    for j in range(y, edge):
        if box[x][j] == taste:
            res.append('R')
    # Left
    for j in range(y, -1, -1):
        if box[x][j] == taste:
            res.append('L')
    # Front
    for i in range(x, -1, -1):
        if box[i][y] == taste:
            res.append('F')
    # Back
    for i in range(x, edge):
        if box[i][y] == taste:
            res.append('B')
    if res:
        return res[randrange(0, len(res))]
    else:
        return False


def distribution_candies(box, x, y, taste):
    # 右方向に貯まっているか
    res_right = 0
    for i in range(edge):
        for j in range(y, edge):
            if box[i][j] == taste:
                res_right += 1
    # 左方向に貯まっているか
    res_left = 0
    for i in range(edge):
        for j in range(y):
            if box[i][j] == taste:
                res_left += 1
    # 前方向に貯まっているか
    res_front = 0
    for i in range(x):
        for j in range(edge):
            if box[i][j] == taste:
                res_front += 1
    # 後方向に貯まっているか
    res_back = 0
    for i in range(x, edge):
        for j in range(edge):
            if box[i][j] == taste:
                res_back += 1
    res = [(res_right, 'R'), (res_left, 'L'),
           (res_front, 'F'), (res_back, 'B')]
    res.sort(reverse=True, key=lambda x: x[0])
    return res[0][1]


for i in range(LIM):
    p = int(input())
    x, y = put_index(box, p)
    taste = t[i]
    res = existsametaste(box, x, y, taste)
    if not res:
        if i < 90:
            res = d[taste]
        else:
            res = distribution_candies(box, x, y, taste)
    print(res, flush=True)
    tilt_box(box, res)
    ans.append(res)

print('--')
print('--')
print('--')
print(*ans, sep="\n")
