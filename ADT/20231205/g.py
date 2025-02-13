from collections import deque
from collections import defaultdict

d = defaultdict(int)
N, M = map(int, input().split())
squares = set()
for i in range(M + 1):
    squares.add(i * i)
d = []
for a in range(1, M + 1):
    if M - pow(a, 2) in squares:
        d.append((a, int((M - pow(a, 2)) ** (1 / 2))))
ans = [[-1] * N for _ in range(N)]
ans[0][0] = 0
q = deque([(0, 0)])
dxy = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
while q:
    vx, vy = q.popleft()
    for a, b in d:
        for dx, dy in dxy:
            nx = vx + a * dx
            ny = vy + b * dy
            if 0 <= nx < N and 0 <= ny < N and ans[nx][ny] == -1:
                ans[nx][ny] = ans[vx][vy] + 1
                q.append((nx, ny))
        for dx, dy in dxy:
            nx = vx + b * dx
            ny = vy + a * dy
            if 0 <= nx < N and 0 <= ny < N and ans[nx][ny] == -1:
                ans[nx][ny] = ans[vx][vy] + 1
                q.append((nx, ny))
for c in ans:
    print(*c)
