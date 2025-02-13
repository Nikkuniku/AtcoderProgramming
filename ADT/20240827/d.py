H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(H):
    for j in range(W):
        for dx, dy in dxy:
            tmp = []
            for k in range(5):
                ni = i + k * dx
                nj = j + k * dy
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                tmp.append(S[ni][nj])
            if len(tmp) == 5 and "".join(tmp) == "snuke":
                for k in range(5):
                    ni = i + k * dx
                    nj = j + k * dy
                    print(ni + 1, nj + 1)
                exit()
