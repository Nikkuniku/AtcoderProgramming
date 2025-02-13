H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)]
x, y = 0, 0
while 1:
    seen[x][y] = True
    S = G[x][y]
    if S == "U":
        if x != 0:
            x -= 1
        else:
            break
    elif S == "D":
        if x != H - 1:
            x += 1
        else:
            break
    elif S == "L":
        if y != 0:
            y -= 1
        else:
            break
    elif S == "R":
        if y != W - 1:
            y += 1
        else:
            break
    if seen[x][y]:
        exit(print(-1))
print(x + 1, y + 1)
