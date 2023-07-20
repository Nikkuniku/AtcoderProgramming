from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
color = [-1]*N
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)


def BFS(s):
    q = deque([(s, 0)])
    while q:
        v, c = q.popleft()
        color[v] = c
        for e in Edge[v]:
            if color[e] == -1:
                color[e] = 1-c
                q.append((e, 1-c))
            else:
                if color[v] == color[e]:
                    return False
    return True


ans = 'Yes'
for v in range(N):
    if color[v] == -1:
        if not BFS(v):
            ans = 'No'
print(ans)
