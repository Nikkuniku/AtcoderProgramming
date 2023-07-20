ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())


def vec(sx, sy, gx, gy):
    return (gx-sx, gy-sy)


def cross(X, Y):
    return X[0]*Y[1]-X[1]*Y[0]


AB = vec(ax, ay, bx, by)
AD = vec(ax, ay, dx, dy)
BA = vec(bx, by, ax, ay)
BC = vec(bx, by, cx, cy)
CB = vec(cx, cy, bx, by)
CD = vec(cx, cy, dx, dy)
DC = vec(dx, dy, cx, cy)
DA = vec(dx, dy, ax, ay)

ans = 'No'
if cross(AD, AB) < 0 and cross(BA, BC) < 0 and cross(CB, CD) < 0 and cross(DC, DA) < 0:
    ans = 'Yes'
print(ans)
