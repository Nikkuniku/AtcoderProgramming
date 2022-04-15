h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]


def outcorner(i, j):
    re = 0
    # 1
    F = True
    for x, y in [(0, -1), (-1, -1), (-1, 0)]:
        if s[i+x][j+y] == '#':
            F = False
    if F:
        re += 1
    # 2
    F = True
    for x, y in [(-1, 0), (-1, 1), (0, 1)]:
        if s[i+x][j+y] == '#':
            F = False
    if F:
        re += 1
    # 3
    F = True
    for x, y in [(0, 1), (1, 1), (1, 0)]:
        if s[i+x][j+y] == '#':
            F = False
    if F:
        re += 1
    # 3
    F = True
    for x, y in [(1, 0), (1, -1), (0, -1)]:
        if s[i+x][j+y] == '#':
            F = False
    if F:
        re += 1
    return re


def incorner(i, j):
    re = 0
    # 1
    cnt = 0
    for x, y in [(0, -1), (1, 0)]:
        if s[i+x][j+y] == '#':
            cnt += 1
    knt = 0
    for x, y in [(0, 0), (1, -1)]:
        if s[i+x][j+y] == '#':
            knt += 1
    if cnt == 1 and knt == 2:
        re += 1
    # 2
    cnt = 0
    for x, y in [(0, 1), (1, 0)]:
        if s[i+x][j+y] == '#':
            cnt += 1
    knt = 0
    for x, y in [(0, 0), (1, 1)]:
        if s[i+x][j+y] == '#':
            knt += 1
    if cnt == 1 and knt == 2:
        re += 1
    return re


ans = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if s[i][j] == '#':
            ans += outcorner(i, j)
            ans += incorner(i, j)
print(ans)
