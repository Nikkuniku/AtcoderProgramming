H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
sx, sy = -1, -1
gx, gy = -1, -1
for i in range(H):
    for j in range(W):
        if S[i][j] != "o":
            continue
        if sx == -1:
            sx = i
            sy = j
        else:
            gx = i
            gy = j
ans = abs(sx - gx) + abs(sy - gy)
print(ans)
