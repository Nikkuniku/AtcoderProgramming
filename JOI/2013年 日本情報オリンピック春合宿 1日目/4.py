
def dist(sx, sy, gx, gy):
    return ((sx-gx)**2+(sy-gy)**2)**(1/2)


def dist_squared(sx, sy, gx, gy):
    return (sx-gx)**2+(sy-gy)**2


N, W, H = map(int, input().split())
Point = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for a in range(N):
    for b in range(N):
        if a == b:
            continue
        A = Point[a]
        B = Point[b]
        ra = dist(*A, *B)
        ra2 = dist_squared(*A, *B)
        if not (ra <= A[0] <= W-ra and ra <= A[1] <= H-ra):
            continue
        for c in range(N):
            if a == c or b == c:
                continue
            for d in range(N):
                if a == d or b == d or c == d:
                    continue
                C = Point[c]
                D = Point[d]
                rc = dist(*C, *D)
                rc2 = dist_squared(*C, *D)
                dis = dist(*A, *C)
                dis2 = dist_squared(*A, *C)
                if 0 < ra2-dis2 - rc2 and 4*rc2*dis2 < (ra2-dis2 - rc2)**2:
                    ans += 1
print(ans)
