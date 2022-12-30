from itertools import combinations
grid = [list(input()) for _ in range(9)]
points = []
for i in range(9):
    for j in range(9):
        if grid[i][j] == '#':
            points.append((i+1, j+1))


def check(p1, p2, p3, p4):
    a = [p1, p2, p3, p4]
    v = []
    for i in range(4):
        for j in range(i+1, 4):
            dx = a[i][0]-a[j][0]
            dy = a[i][1]-a[j][1]
            v.append(dx*dx + dy*dy)
    v = sorted(v)
    L = v[0]
    if L == 0:
        return False
    return v[0] == L and v[1] == L and v[2] == L and v[3] == L and v[4] == 2*L and v[5] == 2*L


C = combinations(points, 4)
ans = 0
for c in C:
    b1, b2, b3, b4 = c
    if check(b1, b2, b3, b4):
        ans += 1
print(ans)
