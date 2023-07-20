from collections import defaultdict
L, N, M = map(int, input().split())
da = defaultdict(list)
db = defaultdict(list)
a = 1
b = 1
for _ in range(N):
    v, l = map(int, input().split())
    da[v].append([a, a+l-1])
    a += l
for _ in range(M):
    v, l = map(int, input().split())
    db[v].append([b, b+l-1])
    b += l
keys = list(set(list(da.keys())+list(db.keys())))
ans = 0
for k in keys:
    i = 0
    j = 0
    while i < len(da[k]) and j < len(db[k]):
        a, b = da[k][i]
        c, d = db[k][j]
        if max(a, c) <= min(b, d):
            ans += min(b, d)-max(a, c)+1
        if b <= d:
            i += 1
        else:
            j += 1
print(ans)
