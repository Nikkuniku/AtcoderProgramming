H, W, N = map(int, input().split())
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
res = [["."] * W for _ in range(H)]
i, j = 0, 0
cnt = 0
direction = 0
while cnt < N:
    if res[i][j] == ".":
        res[i][j] = "#"
        direction += 1
        direction %= 4
    else:
        res[i][j] = "."
        direction -= 1
        direction %= 4
    i += dxy[direction][0]
    j += dxy[direction][1]
    i %= H
    j %= W
    cnt += 1
for c in res:
    print(*c, sep="")
