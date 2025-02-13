N = int(input())
res = []


def dfs(v, c):
    if v > 555555:
        return
    res.append(v)
    dfs(10 * v + c, c)


for i in range(1, 10):
    dfs(i, i)
res.sort()
print(res[N - 1])
