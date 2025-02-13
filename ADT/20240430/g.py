from collections import deque

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
P = [[0] * M for _ in range(N)]
stopped = set()
q = deque([(1, 1)])
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    vx, vy = q.popleft()
    P[vx][vy] = 1
    for dx, dy in dxy:
        nx = vx + dx
        ny = vy + dy
        while 1:
            if S[nx][ny] == ".":
                P[nx][ny] = 1
                nx += dx
                ny += dy
            else:
                nx -= dx
                ny -= dy
                break
        if (nx, ny) in stopped:
            continue
        stopped.add((nx, ny))
        q.append((nx, ny))
ans = sum([sum(P[i]) for i in range(N)])
print(ans)
