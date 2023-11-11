import sys

sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
Edge = [set() for _ in range(N)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
es = [set() for _ in range(N)]
for i in range(M):
    a = A[i] - 1
    b = B[i] - 1
    if b < a:
        a, b = b, a
    es[a].add(b)
    es[b].add(a)
colors = [0 for i in range(N)]


# 頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse
def dfs(v, color):
    # 今いる点を着色
    colors[v] = color
    # 今の頂点から行けるところをチェック
    for to in es[v]:
        # 同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        # 未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    # 調べ終わったら矛盾がないのでTrue
    return True


# 2部グラフならTrue, そうでなければFalse
def is_bipartite():
    for v in range(N):
        if colors[v] != 0:
            continue
        if not dfs(v, 1):
            return False  # 頂点0を黒(1)で塗ってDFS開始
    return True


ans = "Yes" if is_bipartite() else "No"
print(ans)
