from collections import deque
from collections import defaultdict
H, W, N = map(int, input().split())
Grid = [list(input()) for _ in range(H)]
d = defaultdict(int)
for i in range(H):
    for j in range(W):
        if Grid[i][j] in ['.', 'X']:
            continue
        d[Grid[i][j]] = (i, j)


def BFS(sx, sy, gx, gy):
    dist = [[-1]*W for _ in range(H)]
    q = deque([(sx, sy)])
    dist[sx][sy] = 0
    dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while q:
        vx, vy = q.popleft()
        for dx, dy in dxy:
            nx = vx+dx
            ny = vy+dy
            if 0 <= nx < H and 0 <= ny < W:
                if Grid[nx][ny] != 'X' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[vx][vy]+1
                    q.append((nx, ny))
    return dist[gx][gy]


ans = 0
seq = ['S']+[str(i+1) for i in range(N)]
for i in range(len(seq)-1):
    ans += BFS(*d[seq[i]], *d[seq[i+1]])
print(ans)
