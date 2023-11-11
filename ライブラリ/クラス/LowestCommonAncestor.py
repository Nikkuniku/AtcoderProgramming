class LowestCommonAncestor_Doubling:

    def __init__(self, N: int, Edge: list,) -> None:
        '''
        LCAを求めるためのクラス
        Parameters
        ----------
        N:int
        Edge:list[list]
        '''
        self.N = N
        self.depth = [-1]*N
        self.doubling = self._init_Doubling(N, Edge)

    def _init_Doubling(self, N: int, Edge: list) -> list:
        '''
        ダブリング配列作成用（クラスインスタンス作成時実行）
        Parameters
        ----------
        N:int
        Edge:list[list]
        '''
        from collections import deque
        res_doubling = [[-1]*N for _ in range(N.bit_length()+1)]
        que = deque()
        for i in range(N):
            if self.depth[i] != -1:
                continue
            self.depth[i] = 0
            que.append(i)
            while que:
                v = que.popleft()
                for e in Edge[v]:
                    if self.depth[e] != -1:
                        continue
                    self.depth[e] = self.depth[v]+1
                    res_doubling[0][e] = v
                    que.append(e)
        for k in range(1, N.bit_length()+1):
            for v in range(N):
                if res_doubling[k-1][v] == -1:
                    continue
                res_doubling[k][v] = res_doubling[k-1][res_doubling[k-1][v]]
        return res_doubling

    def get_ancestor(self, u: int, i: int) -> int:
        '''
        頂点uから根に向かってiだけ進んだ時の頂点番号
        存在しない場合は-1
        Parameters
        ----------
        u:int
        i:int
        '''
        res_ancestor = u
        for j in range(i.bit_length(), -1, -1):
            if i & (1 << j):
                res_ancestor = self.doubling[j][res_ancestor]
            if res_ancestor == -1:
                break
        return res_ancestor

    def get_lca(self, u: int, v: int) -> int:
        '''
        頂点uと頂点vのLCAを返す
        Parameters
        ----------
        u:int
        v:int
        '''
        d_u = self.depth[u]
        d_v = self.depth[v]
        # vを深い側とする
        if d_u > d_v:
            u, v = v, u
            d_u, d_v = d_v, d_u
        depth_diff = abs(d_u-d_v)
        v = self.get_ancestor(v, depth_diff)
        d_v = d_u
        # 深さが一致した時に点が等しければ、その点自体がLCA
        if u == v:
            return u
        for k in range(d_v.bit_length(), -1, -1):
            next_u = self.doubling[k][u]
            next_v = self.doubling[k][v]
            if next_u != next_v:
                u = next_u
                v = next_v
        lca = self.doubling[0][u]
        return lca

    def get_distance(self, u: int, v: int) -> int:
        '''
        頂点uと頂点vの2点間距離をlcaを使って求める
        Parameters
        ----------
        u:int
        v:int
        '''
        lca = self.get_lca(u, v)
        return self.depth[u]+self.depth[v]-2*self.depth[lca]


N = int(input())
edge = [[] for _ in range(N)]
for i in range(N):
    t, *c = list(map(int, input().split()))
    for to in c:
        edge[i].append(to)

Lcadoubling = LowestCommonAncestor_Doubling(N, edge)
Q = int(input())
ans = []
for _ in range(Q):
    u, v = map(int, input().split())
    ans.append(Lcadoubling.get_lca(u, v))
print(*ans, sep="\n")
