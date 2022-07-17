from collections import deque
n = int(input())
p = list(map(int, input().split()))


kouho = set()


def dfs(arr):
    if tuple(arr) in kouho:
        return
    else:
        kouho.add(tuple(arr))

    arr = deque(arr)
    v = arr.pop()
    arr.appendleft(v)
    dfs(arr)

    arr = list(reversed(arr))
    dfs(arr)


dfs(p)
print(kouho)
