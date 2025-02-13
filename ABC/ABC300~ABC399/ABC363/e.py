from heapq import heappop, heappush

H, W, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
L = 10**5
B = [[] for _ in range(L + 1)]
C = [[False] * W for _ in range(H)]
D = [[False] * W for _ in range(H)]
q = []
res = H * W
ans = []
for i in range(H):
    for j in range(W):
        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            heappush(q, A[i][j])
            B[A[i][j]].append((i, j))
            D[i][j] = True
for i in range(1, Y + 1):
    while q:
        p = heappop(q)
        if p <= i:
            vi, vj = B[p].pop()
            if C[vi][vj]:
                continue
            C[vi][vj] = True
            res -= 1
            for dx, dy in dxy:
                ni = vi + dx
                nj = vj + dy
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if C[ni][nj]:
                    continue
                if D[ni][nj]:
                    continue
                heappush(q, A[ni][nj])
                B[A[ni][nj]].append((ni, nj))
                D[ni][nj] = True
        else:
            heappush(q, p)
            break
    ans.append(res)
print(*ans, sep="\n")
