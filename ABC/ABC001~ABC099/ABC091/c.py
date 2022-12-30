n = int(input())
X = [list(map(int, input().split())) for _ in range(n)]
Y = [list(map(int, input().split())) for _ in range(n)]

edges = [set() for _ in range(n)]
matched = [-1] * n

for i in range(n):
    for j in range(n):
        if X[i][0] < Y[j][0] and X[i][1] < Y[j][1]:
            edges[i].add(j)


def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False


print(sum(dfs(s, set()) for s in range(n)))
