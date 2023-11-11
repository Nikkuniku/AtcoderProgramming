def is_Bipertite(Edge):
    from collections import deque

    N = len(Edge)
    q = deque()
    colors = [-1] * N
    for v in range(N):
        if colors[v] != -1:
            continue
        q.append((v, 0))
        colors[v] = 0
        while q:
            w, c = q.popleft()
            for e in Edge[w]:
                if colors[e] != -1:
                    if colors[e] == c:
                        return False
                else:
                    colors[e] = c ^ 1
                    q.append((e, c ^ 1))
    return True


N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(M):
    Edge[A[i] - 1].append(B[i] - 1)
    Edge[B[i] - 1].append(A[i] - 1)

ans = "Yes" if is_Bipertite(Edge) else "No"
print(ans)
