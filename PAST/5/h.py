from collections import deque

H, W = map(int, input().split())
r, c = map(int, input().split())
r -= 1
c -= 1
S = [list(input()) for _ in range(H)]
q = deque([(r, c)])
dxy = [(-1, 0, "v"), (1, 0, "^"), (0, 1, "<"), (0, -1, ">")]
ans = [["x"] * W for _ in range(H)]
seen = [[False] * W for _ in range(H)]
ans[r][c] = "o"
seen[r][c] = True
while q:
    vx, vy = q.popleft()
    for dx, dy, dir in dxy:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if seen[nx][ny]:
            continue
        if S[nx][ny] == dir or S[nx][ny] == ".":
            ans[nx][ny] = "o"
            seen[nx][ny] = True
            q.append((nx, ny))
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            ans[i][j] = "#"
for c in ans:
    print(*c, sep="")
