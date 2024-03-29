# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
from collections import Counter, deque


def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N

    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

# 縮約後のグラフを構築


def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP


n, m = map(int, input().split())

G = [[] for _ in range(n)]
GR = [[] for _ in range(n)]
edge = [set() for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    GR[v].append(u)
    edge[u].add(v)

l, g = scc(n, G, GR)
print(l, g)
c = Counter(g)
print(c)
groups = scc.scc()
print(groups)
print(construct(n, G, l, g))
