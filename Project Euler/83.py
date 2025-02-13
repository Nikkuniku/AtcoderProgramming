f = open("./0083_matrix.txt", "r")
S = [s.split(",") for s in f.read().split("\n")]
S.pop()
S = [list(map(int, m)) for m in S]
N = len(S)
from heapq import heappop, heappush


def dijkstra(si, sj):
    N = len(S)
    INF = 1 << 60
    dist = [[INF] * N for _ in range(N)]
    dist[si][sj] = S[si][sj]
    q = [(dist[si][sj], si, sj)]
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while q:
        d, vx, vy = heappop(q)
        if dist[vx][vy] != d:
            continue
        for dx, dy in dxy:
            nx = vx + dx
            ny = vy + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if dist[nx][ny] > d + S[nx][ny]:
                dist[nx][ny] = d + S[nx][ny]
                heappush(q, (dist[nx][ny], nx, ny))
    return dist[-1][-1]


ans = dijkstra(0, 0)
print(ans)
