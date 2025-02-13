N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
ans = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        tmp = int(S[i][j] == "#")
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if S[ni][nj] == "#":
                tmp += 1
        ans[i][j] = tmp
for c in ans:
    print(*c, sep="")
