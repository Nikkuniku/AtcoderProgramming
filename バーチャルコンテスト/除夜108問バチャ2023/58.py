from itertools import combinations


def check(X, Y, Z, W):
    v = []
    x = [X[0], Y[0], Z[0], W[0]]
    y = [X[1], Y[1], Z[1], W[1]]
    for i in range(4):
        for j in range(i+1, 4):
            dx = x[i]-x[j]
            dy = y[i]-y[j]
            v.append(dx**2 + dy**2)
    v.sort()
    L = v[0]
    if L == 0:
        return False
    return v[0] == v[1] == v[2] == v[3] == L and v[4] == v[5] == 2*L


S = [input() for _ in range(9)]
points = []
for i in range(9):
    for j in range(9):
        if S[i][j] == '#':
            points.append((i, j))

C = list(combinations(points, 4))
ans = 0
for a, b, c, d in C:
    ans += check(a, b, c, d)
print(ans)
