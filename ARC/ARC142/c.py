N = int(input())
from collections import defaultdict

d1 = defaultdict(int)
d2 = defaultdict(int)
# 頂点1と頂点2を除いた各頂点との距離
for v in range(3, N + 1):
    print("? {0} {1}".format(1, v), flush=True)
    duv = int(input())
    d1[v] = duv
# 頂点2と頂点1を除いた各頂点との距離
for v in range(3, N + 1):
    print("? {0} {1}".format(2, v), flush=True)
    duv = int(input())
    d2[v] = duv
if 1 not in set(d1.values()):
    print("! 1")
if 1 not in set(d2.values()):
    print("! 1")
# 頂点1との距離が1、かつ頂点2との距離が2である頂点集合
M = []
for i, v in d1.items():
    if v == 1 and d2[i] == 2:
        M.append(i)
# 頂点2との距離が1、かつ頂点1との距離が2である頂点集合
L = []
for i, v in d2.items():
    if v == 1 and d1[i] == 2:
        L.append(i)
if M and L:
    # MとLの頂点集合間の距離を確認する
    print("? {} {}".format(M[0], L[0]))
    duv = int(input())
    if duv == 3:
        print("! 1", flush=True)
res = 1 << 60
for v in range(3, N + 1):
    res = min(res, d1[v] + d2[v])
print("! {}".format(res))
