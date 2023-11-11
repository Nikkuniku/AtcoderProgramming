def is_Bipertite(Edge: list([])) -> bool:
    """
    与えられたグラフが2部グラフであるか判定する
    Parameters
    ----------
    Edge:list[]
        グラフの隣接リスト
    Returns
    -------
    result:bool
        true:2部グラフである
        false:2部グラフでない
    """
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
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)

ans = "Yes" if is_Bipertite(Edge) else "No"
print(ans)
