N = int(input())
A = list(map(int, input().split()))
visited = [False] * N
walk = []
v = 0
while not visited[v]:
    visited[v] = True
    walk.append(v)
    v = A[v] - 1
idx = walk.index(v)
cycle = list(map(lambda x: x + 1, walk[idx:]))
print(len(cycle))
print(*cycle)
