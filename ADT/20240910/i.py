N = int(input())
adjacents = [[] for _ in range(N)]
indexForAdjacents = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    indexForAdjacents[u].append(len(adjacents[v]))
    indexForAdjacents[v].append(len(adjacents[u]))
    adjacents[u].append(v)
    adjacents[v].append(u)
childSubTreeRes = [[1] * len(adjacents[i]) for i in range(N)]
nodeRes = [0] * N
parents = [-1] * N
order = []
stack = []
stack.append(0)
while stack:
    node = stack.pop()
    order.append(node)
    for e in adjacents[node]:
        if e == parents[node]:
            continue
        stack.append(e)
        parents[e] = node
print(parents)
print(order)
for i in range(len(order) - 1, 0, -1):
    node = order[i]
    parent = parents[node]
    result = 1
    parentIndex = -1
    for j in range(len(adjacents[node])):
        if adjacents[node][j] == parent:
            parentIndex = j
            continue
        result += childSubTreeRes[node][j]
    childSubTreeRes[parent][indexForAdjacents[node][parentIndex]] = result
print(*childSubTreeRes, sep="\n")
for i in range(len(order)):
    node = order[i]
    accumsFromTail = [0] * len(adjacents[node])
    for j in range(len(accumsFromTail) - 1, 0, -1):
        accumsFromTail[j - 1] += accumsFromTail[j] + childSubTreeRes[node][j]
    accum = 0
    for j in range(len(accumsFromTail)):
        result = accum + accumsFromTail[j]
        childSubTreeRes[adjacents[node][j]][indexForAdjacents[node][j]] = result
        accum += childSubTreeRes[node][j]
        nodeRes[node] = accum
print(nodeRes)
