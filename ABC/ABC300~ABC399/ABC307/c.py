from itertools import combinations, combinations_with_replacement
from collections import defaultdict
from copy import deepcopy


def zahyo(H, W, Z):
    sx, sy = -1, -1
    dz = defaultdict(int)
    for i in range(H):
        for j in range(W):
            if Z[i][j] == '#':
                sx = i
                sy = j
                dz[(i, j)] = 1
    Mz = []
    for ax, ay in dz.keys():
        Mz.append((ax-sx, ay-sy))
    return Mz


def blackCNT(H, W, Z):
    res = 0
    for i in range(H):
        for j in range(W):
            if Z[i][j] == '#':
                res += 1
    return res


Ha, Wa = map(int, input().split())
A = [list(input()) for _ in range(Ha)]
Hb, Wb = map(int, input().split())
B = [list(input()) for _ in range(Hb)]
Hx, Wx = map(int, input().split())
X = [list(input()) for _ in range(Hx)]
Ma = zahyo(Ha, Wa, A)
Mb = zahyo(Hb, Wb, B)
Ca = blackCNT(Ha, Wa, A)
Cb = blackCNT(Hb, Wb, B)
Cx = blackCNT(Hx, Wx, X)
if Cx < Ca or Cx < Cb:
    print('No')
    exit()
C = []
Z = [[0]*Wx for _ in range(Hx)]
for i in range(Hx):
    for j in range(Wx):
        if X[i][j] == '#':
            Z[i][j] = 1
        C.append((i, j))
P = list(combinations_with_replacement(C, 2))
ans = 'No'
for c in P:
    isOK = True
    a, b = c[0][0], c[0][1]
    s, t = c[1][0], c[1][1]
    tmp = [[0]*Wx for _ in range(Hx)]
    for dx, dy in Ma:
        na, nb = a+dx, b+dy
        if 0 <= na < Hx and 0 <= nb < Wx:
            tmp[na][nb] = 1
        else:
            isOK = False
            break
    for dx, dy in Mb:
        ns, nt = s+dx, t+dy
        if 0 <= ns < Hx and 0 <= nt < Wx:
            tmp[ns][nt] = 1
        else:
            isOK = False
            break
    if tmp == Z and isOK:
        ans = 'Yes'
    isOK = True
    a, b = c[1][0], c[1][1]
    s, t = c[0][0], c[0][1]
    tmp = [[0]*Wx for _ in range(Hx)]
    for dx, dy in Ma:
        na, nb = a+dx, b+dy
        if 0 <= na < Hx and 0 <= nb < Wx:
            tmp[na][nb] = 1
        else:
            isOK = False
            break
    for dx, dy in Mb:
        ns, nt = s+dx, t+dy
        if 0 <= ns < Hx and 0 <= nt < Wx:
            tmp[ns][nt] = 1
        else:
            isOK = False
            break
    if tmp == Z and isOK:
        ans = 'Yes'
print(ans)
