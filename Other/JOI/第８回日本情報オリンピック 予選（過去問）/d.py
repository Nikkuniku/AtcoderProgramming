from sys import setrecursionlimit
setrecursionlimit(10**6)
M = int(input())
N = int(input())
G = [[0]*(M+2)]
for _ in range(N):
    G.append([0]+list(map(int, input().split()))+[0])
G.append([0]*(M+2))
ans = 0
dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
seen = [[False]*(M+2) for _ in range(N+2)]


def dfs(vx, vy, d=1, px=-1, py=-1):
    global ans
    ans = max(ans, d)
    seen[vx][vy] = True
    for dx, dy in dxy:
        nx = vx+dx
        ny = vy+dy
        if seen[nx][ny]:
            continue
        if G[nx][ny] == 0:
            continue
        dfs(nx, ny, d+1, vx, vy)
    seen[vx][vy] = False


for i in range(N+2):
    for j in range(M+2):
        if G[i][j] == 0:
            continue
        dfs(i, j)
print(ans)
