import sys


def Loading_Search(N, H, x, y, cnt):
    Sands = []
    for i in range(N):
        for j in range(N):
            if H[i][j] <= 0:
                continue
            Sands.append((H[i][j], abs(i - x) + abs(j - y), i, j))
    if cnt == 0:
        Sands.sort(key=lambda x: x[0], reverse=True)
    Sands.sort(key=lambda x: x[1])
    if not Sands:
        return False, -1, -1, -1, []
    d = Sands[0][0]
    px, py = Sands[0][2:]
    return True, d, px, py, Sands


def movement(sx, sy, gx, gy):
    res = []
    for _ in range(abs(sx - gx)):
        if sx - gx > 0:
            res.append("U")
        else:
            res.append("D")
    for _ in range(abs(sy - gy)):
        if sy - gy > 0:
            res.append("L")
        else:
            res.append("R")
    return res


N = int(input())
H = [list(map(int, input().split())) for _ in range(N)]
ans = []
x, y = 0, 0
while 1:
    luggage = 0
    isOK = True
    for k in range(14):
        res, d, px, py, Sands = Loading_Search(N, H, x, y, k)
        if not res:
            if k == 0:
                isOK = False
            break
        if k > 0 and abs(x - px) + abs(y - py) > 6:
            break
        luggage += d
        ans += movement(x, y, px, py)
        x, y = px, py
        ans.append("+{}".format(d))
        H[px][py] = 0
    if not isOK:
        break
    while luggage:
        Negs = []
        for i in range(N):
            for j in range(N):
                if H[i][j] >= 0:
                    continue
                Negs.append((H[i][j], abs(i - x) + abs(j - y), i, j))
        Negs.sort(key=lambda x: x[1])
        target = Negs[0][0]
        qx, qy = Negs[0][2:]
        ans += movement(x, y, qx, qy)
        x, y = qx, qy
        if luggage + target >= 0:
            luggage += target
            H[qx][qy] = 0
            ans.append("{}".format(target))
        else:
            H[qx][qy] += luggage
            ans.append("-{}".format(luggage))
            luggage = 0


print(*ans, sep="\n")
