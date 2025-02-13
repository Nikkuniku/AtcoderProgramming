def check(X, Y, Z, W):
    v = []
    x = [X[0], Y[0], Z[0], W[0]]
    y = [X[1], Y[1], Z[1], W[1]]
    for i in range(4):
        for j in range(i + 1, 4):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            v.append(dx**2 + dy**2)
    v.sort()
    L = v[0]
    if L == 0:
        return False
    return v[0] == v[1] == v[2] == v[3] == L and v[4] == v[5] == 2 * L


N = int(input())
Points = []
PointsSet = set()
for _ in range(N):
    a, b = map(int, input().split())
    Points.append((a, b))
    PointsSet.add((a, b))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        xa, ya = Points[i]
        xc, yc = Points[j]
        xb = ((xa + xc) / 2) + ((yc - ya) / 2)
        yb = ((ya + yc) / 2) - ((xc - xa) / 2)
        xd = ((xa + xc) / 2) - ((yc - ya) / 2)
        yd = ((ya + yc) / 2) + ((xc - xa) / 2)
        if not xb.is_integer():
            continue
        if not yb.is_integer():
            continue
        if not xd.is_integer():
            continue
        if not yd.is_integer():
            continue
        xb = int(xb)
        yb = int(yb)
        xd = int(xd)
        yd = int(yd)
        if (xb, yb) in PointsSet and (xd, yd) in PointsSet:
            if not check((xa, ya), (xb, yb), (xc, yc), (xd, yd)):
                continue
            tmp = ((xc - xa) ** 2 + (yc - ya) ** 2) // 2
            ans = max(ans, tmp)
print(ans)
