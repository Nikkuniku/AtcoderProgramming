from itertools import permutations
from sys import setrecursionlimit
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
setrecursionlimit(10**8)
N, H, W = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]


def check(Tiles, Wariate, cnt):
    si, sj = -1, -1
    for i in range(H):
        for j in range(W):
            if Wariate[i][j] == -1:
                si = i
                sj = j
                break
        if si != -1 and sj != -1:
            break
    if (si, sj) == (-1, -1):
        exit(print("Yes"))
    if cnt >= len(Tiles):
        return False

    Ta, Tb = Tiles[cnt]

    isOK = True
    for x in range(si, si + Ta):
        for y in range(sj, sj + Tb):
            if not (0 <= x < H and 0 <= y < W):
                isOK = False
                break
            if Wariate[x][y] != -1:
                isOK = False
                break
        if not isOK:
            break
    if isOK:
        for x in range(si, si + Ta):
            for y in range(sj, sj + Tb):
                Wariate[x][y] = 1
        check(Tiles, Wariate, cnt + 1)
        for x in range(si, si + Ta):
            for y in range(sj, sj + Tb):
                Wariate[x][y] = -1
    if Ta != Tb:
        isOK_90 = True
        for x in range(si, si + Tb):
            for y in range(sj, sj + Ta):
                if not (0 <= x < H and 0 <= y < W):
                    isOK_90 = False
                    break
                if Wariate[x][y] != -1:
                    isOK_90 = False
                    break
            if not isOK_90:
                break
        if isOK_90:
            for x in range(si, si + Tb):
                for y in range(sj, sj + Ta):
                    Wariate[x][y] = 1
            check(Tiles, Wariate, cnt + 1)
            for x in range(si, si + Tb):
                for y in range(sj, sj + Ta):
                    Wariate[x][y] = -1


for i in range(1, 1 << N):
    kouho = []
    for j in range(N):
        if i & (1 << j):
            kouho.append(T[j])
    P = list(permutations(kouho))
    for p in P:
        init = [[-1] * W for _ in range(H)]
        check(p, init, 0)
print("No")
