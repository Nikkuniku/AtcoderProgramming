import sys
sys.setrecursionlimit(10**6)
n = int(input())
sts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

ans = []


def dfs(s, depth):
    if depth == n:
        ans.append(s)
        return

    kinds = len(set(list(s)))
    for i in range(kinds+1):
        t = s + sts[i]
        dfs(t, depth+1)


dfs('', 0)
print(*ans, sep="\n")
