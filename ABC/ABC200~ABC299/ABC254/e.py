from collections import defaultdict, deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    Edge[a].append(b)
    Edge[b].append(a)


def solve(y, kyori):
    dist = defaultdict(int)
    dist[y] = 0
    q = deque([y])
    while q:
        v = q.popleft()
        if dist[v] == kyori:
            continue
        for e in Edge[v]:
            if dist[e] == 0:
                dist[e] = dist[v]+1
                if dist[e] == kyori:
                    continue
                q.append(e)

    res = 0
    for key, val in dist.items():
        if val <= kyori:
            res += key+1
    return res


Q = int(input())
ans = []
for _ in range(Q):
    x, k = map(int, input().split())
    x -= 1
    ans.append(solve(x, k))

print(*ans, sep="\n")
