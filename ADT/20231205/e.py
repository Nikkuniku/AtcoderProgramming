H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = [0] * (min(H, W) + 1)
dxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
for i in range(H):
    for j in range(W):
        if C[i][j] == ".":
            continue
        for k in range(min(H, W) + 1):
            tmp = 0
            for dx, dy in dxy:
                ni = i + dx * k
                nj = j + dy * k
                if 0 <= ni < H and 0 <= nj < W and C[ni][nj] == "#":
                    tmp += 1
            if tmp < 4:
                break
        ans[k - 1] += 1
print(*ans[1:])
