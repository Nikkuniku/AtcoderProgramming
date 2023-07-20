H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dxy = [(0, 0), (1, 0), (0, 1), (1, 1)]
ansx = -1
ansy = -1
for i in range(H):
    for j in range(W):
        cookies = 0
        for dx, dy in dxy:
            ni = i+dx
            nj = j+dy
            if 0 <= ni < H and 0 <= nj < W:
                if S[ni][nj] == '#':
                    cookies += 1
        if cookies == 3:
            for dx, dy in dxy:
                ni = i+dx
                nj = j+dy
                if 0 <= ni < H and 0 <= nj < W:
                    if S[ni][nj] == '.':
                        ansx = ni
                        ansy = nj
                        break
            break
print(ansx+1, ansy+1)
