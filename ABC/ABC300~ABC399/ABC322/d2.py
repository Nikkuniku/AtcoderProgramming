from sys import setrecursionlimit

setrecursionlimit(10**8)

P1 = [list(input()) for _ in range(4)]
P2 = [list(input()) for _ in range(4)]
P3 = [list(input()) for _ in range(4)]


def trimming(A):
    res = []
    for s in A:
        if "".join(s) == "....":
            continue
        res.append(s)
    res2 = [[] for _ in range(len(res))]
    for j in range(4):
        tmp = []
        for i in range(len(res)):
            tmp.append(res[i][j])
        if "".join(tmp) == "." * len(res):
            continue
        for i in range(len(res)):
            res2[i].append(res[i][j])
    return res2


def matrix_rotate90degree_toright(A: list) -> list:
    """
    2次元リストの90度右回転
    Parameters
    ----------
    A:any[][]
    """
    return [list(x) for x in zip(*A[::-1])]


TP1 = trimming(P1)
TP2 = trimming(P2)
TP3 = trimming(P3)


def dfs(Polyomino, Wariate, cnt):
    if cnt == 2:
        for i in range(len(Wariate)):
            for j in range(len(Wariate[i])):
                if Wariate[i][j] == -1:
                    return False
        exit(print("Yes"))
    P = Polyomino[cnt]
    for _ in range(4):
        P = matrix_rotate90degree_toright(P)
        for si in range(4):
            for sj in range(4):
                N = len(P)
                M = len(P[0])
                isOK = True
                for x in range(N):
                    for y in range(M):
                        # 範囲外
                        if not (0 <= si + x < 4 and 0 <= sj + y < 4):
                            isOK = False
                            break
                        # 置けないパターン
                        if P[x][y] == "#" and Wariate[si + x][sj + y] != -1:
                            isOK = False
                            break
                    if not isOK:
                        break

                if not isOK:
                    continue

                for x in range(si, si + N):
                    for y in range(sj, sj + M):
                        if P[x - si][y - sj] == "#":
                            Wariate[x][y] = 1
                dfs(Polyomino, Wariate, cnt + 1)
                for x in range(si, si + N):
                    for y in range(sj, sj + M):
                        if P[x - si][y - sj] == "#":
                            Wariate[x][y] = -1


Polynomios = [TP2, TP3]
init = P1
for i in range(4):
    for j in range(4):
        if init[i][j] == ".":
            init[i][j] = -1
        else:
            init[i][j] = 1
dfs(Polynomios, init, 0)
print("No")
