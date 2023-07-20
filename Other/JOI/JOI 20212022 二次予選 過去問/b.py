from collections import deque
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
q = deque([(0, 0)])
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dist = [[-1]*W for _ in range(H)]
dist[0][0] = 0
while q:
    vx, vy = q.popleft()
    for dx, dy in dxy:
        nx, ny = vx+dx, vy+dy
        if 0 <= nx < H and 0 <= ny < W:
            if S[nx][ny] != S[vx][vy] and dist[nx][ny] == -1:
                dist[nx][ny] = dist[vx][vy]+1
                q.append((nx, ny))
ans = dist[H-1][W-1]
print(ans)
