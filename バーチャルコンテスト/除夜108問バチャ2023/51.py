
def dist(sx, sy, gx, gy):
    return (abs(sx-gx)**2 + abs(sy-gy)**2)**0.5


N, K = map(int, input().split())
A = set(list(map(lambda x: int(x)-1, input().split())))
points = [list(map(int, input().split())) for _ in range(N)]
distance = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        distance[i][j] = dist(*points[i], *points[j])
        distance[j][i] = dist(*points[i], *points[j])
l = 0
r = 3000000
for _ in range(100):
    mid = (l+r)/2
    s = set()
    for k in A:
        s.add(k)
        for j in range(N):
            if j in A:
                continue
            if distance[k][j] < mid:
                s.add(j)

    if len(s) == N:
        r = mid
    else:
        l = mid
print(r)
