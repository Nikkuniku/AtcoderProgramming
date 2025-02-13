from collections import deque

N = int(input())
S = [list(input()) for _ in range(N)]


# red
def f(sx, sy, c):
    dist = [[-1] * N for _ in range(N)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        vx, vy = q.popleft()
        for dx, dy in dxy:
            nx = vx + dx
            ny = vy + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if dist[nx][ny] != -1:
                continue
            if S[nx][ny] != c:
                dist[nx][ny] = dist[vx][vy] + 1
                q.append((nx, ny))
            else:
                dist[nx][ny] = dist[vx][vy]
                q.appendleft((nx, ny))
    return dist


red = f(0, 0, "R")
blue = f(0, N - 1, "B")
ans = red[N - 1][N - 1] + blue[N - 1][0]
print(ans)
