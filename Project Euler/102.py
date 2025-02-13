def get_vector(px, py, qx, qy):
    return qx - px, qy - py


def get_cross(px, py, qx, qy):
    return px * qy - py * qx


def solve(ax, ay, bx, by, cx, cy):
    ab = get_vector(ax, ay, bx, by)
    bc = get_vector(bx, by, cx, cy)
    ca = get_vector(cx, cy, ax, ay)
    a0 = get_vector(ax, ay, 0, 0)
    b0 = get_vector(bx, by, 0, 0)
    c0 = get_vector(cx, cy, 0, 0)
    p, q, r = get_cross(*ab, *b0), get_cross(*bc, *c0), get_cross(*ca, *a0)
    if (p > 0 and q > 0 and r > 0) or (p < 0 and q < 0 and r < 0):
        return True
    return False


f = open("./0102_triangles.txt", "r")
S = f.read().split("\n")
S.pop()
S = [list(map(int, s.split(","))) for s in S]
ans = 0
for ax, ay, bx, by, cx, cy in S:
    ans += solve(ax, ay, bx, by, cx, cy)
print(ans)
