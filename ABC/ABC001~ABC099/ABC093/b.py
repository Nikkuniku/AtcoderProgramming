A, B, K = map(int, input().split())
res = set()
for i in range(K):
    res.add(min(A + i, B))
    res.add(max(A, B - i))
res = sorted(res)
print(*res, sep="\n")
