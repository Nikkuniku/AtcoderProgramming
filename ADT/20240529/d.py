H, W, N = map(int, input().split())
ans = [["."] * W for _ in range(H)]
x, y = 0, 0
dir = 0
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for _ in range(N):
    if ans[x][y] == ".":
        ans[x][y] = "#"
        dir += 1
    else:
        ans[x][y] = "."
        dir -= 1
    dir %= 4
    dx, dy = dxy[dir]
    x += dx
    y += dy
    x %= H
    y %= W
for c in ans:
    print(*c, sep="")
