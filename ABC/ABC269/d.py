from collections import deque
from collections import defaultdict
n = int(input())
masu = set()
point = []
d = defaultdict(lambda: -1)
for _ in range(n):
    x, y = map(int, input().split())
    masu.add((x, y))
    point.append((x, y))

q = deque()
ans = 0
dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]
for i in range(n):
    q.append(point[i])
    if d[point[i]] == -1:
        d[point[i]] = 0
        ans += 1
    else:
        continue

    while q:
        vx, vy = q.popleft()

        for k in range(6):
            nx = vx+dx[k]
            ny = vy+dy[k]
            if (nx, ny) not in masu:
                continue

            if d[(nx, ny)] == -1:
                d[(nx, ny)] = d[(vx, vy)]+1
                q.append((nx, ny))

print(ans)
