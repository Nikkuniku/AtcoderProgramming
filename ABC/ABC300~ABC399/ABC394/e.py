from collections import defaultdict, deque

N = int(input())
G = [[] for _ in range(N)]
revG = [defaultdict(list) for _ in range(N)]
P = []
for i in range(N):
    C = list(input())
    for j in range(N):
        if C[j] == "-":
            continue
        G[i].append((j, C[j]))
        revG[j][C[j]].append(i)
    P.append(C)
ans = [[-1] * N for _ in range(N)]

q = deque()
dist = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            q.appendleft((i, j))
            dist[i][j] = 0
        elif P[i][j] != "-":
            q.append((i, j))
            dist[i][j] = 1
while q:
    x, y = q.popleft()
    for to, lab in G[y]:
        for fr in revG[x][lab]:
            if dist[fr][to] != -1:
                continue
            dist[fr][to] = dist[x][y] + 2
            q.append((fr, to))
for c in dist:
    print(*c)
