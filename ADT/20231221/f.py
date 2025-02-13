def check(arr):
    dist = []
    for i in range(4):
        for j in range(i + 1, 4):
            x = arr[i]
            y = arr[j]
            dx = x[0] - y[0]
            dy = x[1] - y[1]
            dist.append(dx * dx + dy * dy)
    dist.sort()
    l = dist[0]
    if l == 0:
        return False
    return (
        dist[0] == l
        and dist[1] == l
        and dist[2] == l
        and dist[3] == l
        and dist[4] == 2 * l
        and dist[5] == 2 * l
    )


S = [list(input()) for _ in range(9)]
points = []
for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            points.append((i, j))
from itertools import combinations

ans = 0
for c in combinations(points, 4):
    if check([c[0], c[1], c[2], c[3]]):
        ans += 1
print(ans)
