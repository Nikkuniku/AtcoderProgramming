N = int(input())
ans = []


def dfs(v):
    if v > N:
        return
    if set(list(str(v))) == set(["3", "5", "7"]):
        ans.append(v)
    for w in [3, 5, 7]:
        dfs(10 * v + w)


dfs(0)
print(len(ans))
