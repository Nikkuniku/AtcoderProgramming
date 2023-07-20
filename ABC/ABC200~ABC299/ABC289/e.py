from collections import deque


def solve(N, C, Edge):
    adj = [[] for _ in range(N)]
    dist = [[-1]*N for _ in range(N)]
    for u, v in Edge:
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    q = deque()
    q.append((0, N-1))
    dist[0][N-1] = 0
    while q:
        a, b = q.popleft()
        takahashi = [[], []]
        aoki = [[], []]
        # 高橋君が行けるところ
        for e in adj[a]:
            takahashi[C[e]].append(e)
        # 青木君が行けるところ
        for e in adj[b]:
            aoki[C[e]].append(e)
        # 二人の色が異なるように遷移する。
        for i in range(2):
            for v in takahashi[i]:
                for w in aoki[1-i]:
                    if dist[v][w] == -1:
                        dist[v][w] = dist[a][b]+1
                        q.append((v, w))
    return dist[N-1][0]


ans = []
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    inputEdge = [list(map(int, input().split())) for _ in range(m)]
    ans.append(solve(n, c, inputEdge))
print(*ans, sep="\n")
