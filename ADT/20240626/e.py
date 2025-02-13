H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
N = min(H, W)
ans = [0] * (N + 1)
dxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue
        for k in range(N + 1):
            isOK = True
            for di, dj in dxy:
                ni = i + di * k
                nj = j + dj * k
                if not (0 <= ni < H and 0 <= nj < W):
                    isOK = False
                    break
                if S[ni][nj] == ".":
                    isOK = False
                    break
            if not isOK:
                k -= 1
                break
        ans[k] += 1
print(*ans[1:])
