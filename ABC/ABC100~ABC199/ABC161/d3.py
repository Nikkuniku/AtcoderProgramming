from sys import setrecursionlimit


def dfs(v):
    if v > 3234566667:
        return
    res.append(v)
    m = v % 10
    for r in [m - 1, m, m + 1]:
        if abs(m - (r % 10)) <= 1:
            dfs(10 * v + r)


setrecursionlimit(10**8)
K = int(input())
res = []
for p in range(1, 10):
    dfs(p)
res.sort()
ans = res[K - 1]
print(ans)
