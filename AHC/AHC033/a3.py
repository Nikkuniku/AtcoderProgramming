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


def mod_search(S):
    mod_max = [N] * N
    for i in range(N):
        for j in range(N):
            if S[i][j] == -1:
                continue
            mod_max[S[i][j] // N] = min(mod_max[S[i][j] // N], S[i][j] % N)
    return mod_max


def minmod_search(S, tar_div):
    mod = N
    for i in range(N):
        for j in range(N):
            if S[i][j] == -1:
                continue
            if S[i][j] // N != tar_div:
                continue
            mod = min(mod, S[i][j] % N)
    for j in range(N - 1, -1, -1):
        for i in range(N):
            if S[i][j] == -1:
                continue
            if S[i][j] // N != tar_div:
                continue
            if S[i][j] % N == mod:
                return i, j


def make_space(S, sx, sy):
    for i in range(N):
        for j in range(N):
            if j == N - 1:
                continue
            if i == sx and j == sy:
                continue
            if S[i][j] == -1:
                return i, j


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Moves = [[] for _ in range(N)]
# 初期配置
S = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N - 1):
        if 3 - j > 0:
            Moves[i].append("P")
            Moves[i].append("R" * (3 - j))
            Moves[i].append("Q")
            if 3 - j > 1:
                Moves[i].append("L" * (3 - j))
        S[i][3 - j] = A[i][j]
# 余りが0である者を探索
isExistminmod = False
for i in range(N):
    for j in range(N):
        if S[i][j] == -1:
            continue
        if S[i][j] % N == 0:
            isExistminmod = True
Moves[2].append("B")
Moves[3].append("B")
Moves[4].append("B")
c = 1
A_cnt = [1] * N
if not isExistminmod:
    Moves[c].append("RRRPR.")
    Moves[0].append("DPRRRQ")
    S[c][1] = A[c][N - 1]
    A_cnt[c] -= 1
    if S[c][1] // 5 == c:
        Moves[c].append("UQB")
    else:
        Moves[c].append(".")
    Moves[0].append("L")
    Moves[0].append("LLP")
    Moves[c].append("...")
else:
    Moves[c].append("B")
sx, sy = 0, 1
isEnd = [0] * N
while not min(isEnd) >= 5:
    mods = mod_search(S)
    target_div = -1
    for i in range(N):
        if isEnd[i] == 5:
            continue
        if isEnd[i] == mods[i]:
            target_div = i
            break
    if target_div != -1:
        gx, gy = minmod_search(S, target_div)
    else:
        gy = 0
        for gx in range(N):
            if S[gx][gy] != -1 and A_cnt[gx] > 0:
                break
        movement = command(sx, sy, gx, gy)
        Moves[0] += movement
        sx, sy = gx, gy
        gx, gy = make_space(S, sx, sy)
        Moves[0].append("P")
        S[gx][gy], S[sx][sy] = S[sx][sy], S[gx][gy]
        S[sx][sy] = A[sx][-1]
        A_cnt[sx] -= 1
        movement = command(sx, sy, gx, gy)
        Moves[0] += movement
        sx, sy = gx, gy
        Moves[0].append("Q")
        continue
    movement = command(sx, sy, gx, gy)
    Moves[0] += movement
    S[gx][gy] = -1
    if gy == 0 and A_cnt[gx] > 0:
        S[gx][gy] = A[gx][N - 1]
        A_cnt[gx] -= 1
    Moves[0].append("P")
    sx, sy = gx, gy
    movement = command(sx, sy, target_div, N - 1)
    Moves[0] += movement
    Moves[0].append("Q")
    isEnd[target_div] += 1
    sx, sy = target_div, N - 1
for c in Moves:
    print(*c, sep="")
