N = int(input())
dist_1 = [-1] * (N + 1)
for i in range(2, N + 1):
    print("?", 1, i, flush=True)
    d = int(input())
    dist_1[i] = d
v = dist_1.index(max(dist_1))
ans = -1
for i in range(1, N + 1):
    if i == v:
        continue
    print("?", v, i, flush=True)
    d = int(input())
    ans = max(ans, d)
print("!", ans)
