N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
Color = [list(map(int, input().split())) for _ in range(N)]
Grids = [[0]*(C+1) for _ in range(3)]
for i in range(N):
    for j in range(N):
        Grids[(i+j+2) % 3][Color[i][j]] += 1
ans = 1 << 32
for c1 in range(1, C+1):
    for c2 in range(1, C+1):
        for c3 in range(1, C+1):
            if c1 == c2 or c2 == c3 or c1 == c3:
                continue
            tmp = 0
            for j in range(1, C+1):
                tmp += Grids[0][j]*(D[j-1][c1-1])
                tmp += Grids[1][j]*(D[j-1][c2-1])
                tmp += Grids[2][j]*(D[j-1][c3-1])
            ans = min(ans, tmp)
print(ans)
