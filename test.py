def BFS01_NG(N, Edge):
    from collections import deque

    init = -1
    dist = [init] * N
    q = deque([(0, 0)])
    dist[0] = 0
    while q:
        print(q)
        v, d = q.popleft()
        for e, c in Edge[v]:
            if dist[e] != init:
                continue
            dist[e] = dist[v] + c
            if c == 0:
                q.appendleft((e, dist[e]))
            else:
                q.append((e, dist[e]))
    return dist


def BFS01_OK(N, Edge):
    from collections import deque

    init = 1 << 60
    dist = [init] * N
    q = deque([0])
    dist[0] = 0
    while q:
        v = q.popleft()
        for e, c in Edge[v]:
            if dist[v] + c >= dist[e]:
                continue
            dist[e] = dist[v] + c
            if c == 0:
                q.appendleft(e)
            else:
                q.append(e)
    return dist


N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c))
    Edge[b].append((a, c))
print(BFS01_NG(N, Edge))
print(BFS01_OK(N, Edge))
