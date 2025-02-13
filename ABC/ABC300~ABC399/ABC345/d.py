from itertools import product, permutations
from sys import setrecursionlimit

setrecursionlimit(10**8)
N, H, W = map(int, input().split())
Tile = [list(map(int, input().split())) for _ in range(N)]


def check(UseTile, Wariate, cnt):
    if cnt == len(UseTile):
        for i in range(H):
            for j in range(W):
                if Wariate[i][j] == -1:
                    return False
        exit(print("Yes"))
    Ta, Tb = UseTile[cnt]
    for i in range(H):
        for j in range(W):
            isOK = True
            for x in range(i, i + Ta):
                for y in range(j, j + Tb):
                    if not (0 <= x < H and 0 <= y < W):
                        isOK = False
                        break
                    if Wariate[x][y] != -1:
                        isOK = False
                        break
                if not isOK:
                    break
            if not isOK:
                continue
            for x in range(i, i + Ta):
                for y in range(j, j + Tb):
                    Wariate[x][y] = 1
            check(UseTile, Wariate, cnt + 1)
            for x in range(i, i + Ta):
                for y in range(j, j + Tb):
                    Wariate[x][y] = -1


for i in range(1 << N):
    Use = []
    for j in range(N):
        if i & (1 << j):
            Use.append(Tile[j])
    if not Use:
        continue
    P = list(product([0, 1], repeat=len(Use)))
    tmp = 0
    for a, b in Use:
        tmp += a * b
    if tmp != H * W:
        continue
    for p in P:
        UseTiles2 = []
        for j in range(len(Use)):
            a, b = Use[j]
            if p[j] == 0:
                UseTiles2.append((a, b))
            else:
                UseTiles2.append((b, a))
        init = [[-1] * W for _ in range(H)]
        check(UseTiles2, init, 0)
print("No")
