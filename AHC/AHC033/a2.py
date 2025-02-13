def command(sx, sy, gx, gy):
    res = []
    for _ in range(abs(sx - gx)):
        if sx <= gx:
            res.append("D")
        else:
            res.append("U")
    for _ in range(abs(sy - gy)):
        if sy <= gy:
            res.append("R")
        else:
            res.append("L")
    return res


def target_search(S, div, mod):
    for i in range(N):
        for j in range(N):
            if S[i][j] // N == div and S[i][j] % N == mod:
                return i, j


def div_search(S, seen, dictonary):
    for i in range(N):
        for j in range(N):
            if S[i][j] == -1:
                continue
            if seen[S[i][j] // N]:
                continue
            if dictonary[S[i][j] // N] == 5 and S[i][j] % N == 4:
                P.append((i, j))


def mod_search(S):
    mod_max = [-1] * N
    for i in range(N):
        for j in range(N):
            if S[i][j] == -1:
                continue
            mod_max[S[i][j] // N] = max(mod_max[S[i][j] // N], S[i][j] % N)
    return mod_max


from collections import defaultdict

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Moves = [[] for _ in range(N)]
# 初期配置
S = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N - 1):
        Moves[i].append("P")
        Moves[i].append("R" * (3 - j))
        Moves[i].append("Q")
        Moves[i].append("L" * (3 - j))
        S[i][3 - j] = A[i][j]
print(*S, sep="\n")
# 余りがN-1である者を探索
P = []
d = defaultdict(int)
seen = [False] * N
for i in range(N):
    for j in range(N):
        if S[i][j] == -1:
            continue
        d[S[i][j] // N] += 1
for i in range(N):
    for j in range(N):
        if S[i][j] == -1:
            continue
        if d[S[i][j] // N] == 5 and S[i][j] % N == 4:
            seen[S[i][j] // N] = True
            P.append((i, j))
Moves[2].append("B")
Moves[3].append("B")
Moves[4].append("B")
c = 1
A_cnt = [1] * N
if not P:
    Moves[c].append("RRRPR.")
    Moves[0].append("DPRRRQ")
    S[c][1] = A[c][N - 1]
    A_cnt[c] -= 1
    if S[c][1] // 5 == c:
        Moves[c].append("U")
    else:
        Moves[c].append(".")
    Moves[0].append("L")
    Moves[0].append("LLP")
    Moves[c].append("...")
else:
    Moves[c].append("B")
sx, sy = 0, 0
while P:
    gx, gy = P.pop()
    div = S[gx][gy] // N
    mod = S[gx][gy] % N
    while mod >= 0:
        gx, gy = target_search(S, div, mod)
        movement = command(sx, sy, gx, gy)
        Moves[0] += movement
        S[gx][gy] = -1
        if gy == 0 and A_cnt[gx] > 0:
            S[gx][gy] = A[gx][N - 1]
            d[S[gx][gy] // N] += 1
            A_cnt[gx] -= 1
            if d[S[gx][gy] // N] == 5:
                div_search(S, seen, d)
            if S[gx][gy] % 5 == 4:
                P.append((gx, gy))
        Moves[0].append("P")
        sx, sy = gx, gy
        movement = command(sx, sy, div, N - 1)
        Moves[0] += movement
        Moves[0].append("Q")
        sx, sy = div, N - 1
        mod -= 1
for c in Moves:
    print(*c, sep="")
