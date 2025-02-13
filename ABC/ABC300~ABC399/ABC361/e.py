from collections import deque

N = int(input())
edges = [[] for _ in range(N)]
S = 0
for _ in range(N - 1):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))
    S += c


def BFS(s):
    dist = [-1] * N
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for e, cost in edges[v]:
            if dist[e] != -1:
                continue
            dist[e] = dist[v] + cost
            q.append(e)
    return dist


dists = BFS(0)
j = dists.index(max(dists))
dists2 = BFS(j)
mindist = max(dists2)
ans = 2 * S - mindist
print(ans)
