from bisect import bisect_left
from itertools import accumulate

N, M, Q = map(int, input().split())
Goods = []
Goodsbynum = [[] for _ in range(M + 1)]
GoodsOrd = [[] for _ in range(M + 1)]
for i in range(N):
    P, A = map(int, input().split())
    Goods.append(P)
    Goodsbynum[A].append(P)
    GoodsOrd[A].append(i)
Cum_Goods = list(accumulate(Goods, initial=0))
Cum_GoodsByOrd = [[] for _ in range(M + 1)]
for i in range(M + 1):
    Cum_GoodsByOrd[i] = list(accumulate(Goodsbynum[i], initial=0))
ans = []
for _ in range(Q):
    T, L, R = map(int, input().split())
    tmp = Cum_Goods[R] - Cum_Goods[L - 1]
    r = bisect_left(GoodsOrd[T], R)
    l = bisect_left(GoodsOrd[T], L - 1)
    wari = Cum_GoodsByOrd[T][r] - Cum_GoodsByOrd[T][l]
    tmp -= (wari) // 2
    ans.append(tmp)
print(*ans, sep="\n")
