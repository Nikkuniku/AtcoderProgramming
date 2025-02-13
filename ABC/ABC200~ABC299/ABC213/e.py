from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
q = deque([(0, 0)])
INF = 1 << 60
dist = [[INF] * W for _ in range(H)]
dist[0][0] = 0
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    vx, vy = q.popleft()
    # 上下左右
    for dx, dy in dxy:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if dist[nx][ny] <= dist[vx][vy]:
            continue
        if S[nx][ny] == ".":
            dist[nx][ny] = dist[vx][vy]
            q.appendleft((nx, ny))
    # 壁を壊す
    for dx in range(-2, 3, 1):
        for dy in range(-2, 3, 1):
            if abs(dx) == 2 and abs(dy) == 2:
                continue
            nx = vx + dx
            ny = vy + dy
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if dist[nx][ny] <= dist[vx][vy] + 1:
                continue
            dist[nx][ny] = dist[vx][vy] + 1
            q.append((nx, ny))
ans = dist[-1][-1]
print(ans)
