N = int(input())
adjacents = [[] for _ in range(N)]
indexForAdjacents = [[] for _ in range(N)]
for _ in range(N - 1):
    s, t, w = map(int, input().split())
    indexForAdjacents[s].append(len(adjacents[t]))
    indexForAdjacents[t].append(len(adjacents[s]))
    adjacents[s].append((t, w))
    adjacents[t].append((s, w))
childSubTreeRes = [[0] * len(adjacents[i]) for i in range(N)]
nodeRes = [0] * N
parents = [-1] * N
order = []
stack = [0]
while stack:
    node = stack.pop()
    order.append(node)
    for e, _ in adjacents[node]:
        if e == parents[node]:
            continue
        stack.append(e)
        parents[e] = node
for i in range(len(order) - 1, 0, -1):
    node = order[i]
    parent = parents[node]
    result = 0
    parentIndex = -1
    for j in range(len(adjacents[node])):
        if adjacents[node][j][0] == parent:
            parentIndex = j
            continue
        result = max(result, childSubTreeRes[node][j])
    cost = adjacents[parent][indexForAdjacents[node][parentIndex]][1]
    childSubTreeRes[parent][indexForAdjacents[node][parentIndex]] = result + cost

for i in range(len(order)):
    node = order[i]
    accumsFromTail = [0] * len(adjacents[node])
    for j in range(len(accumsFromTail) - 1, 0, -1):
        accumsFromTail[j - 1] = max(childSubTreeRes[node][j], accumsFromTail[j])
    accum = 0
    for j in range(len(accumsFromTail)):
        e = adjacents[node][j][0]
        cost = adjacents[node][j][1]
        result = max(accum, accumsFromTail[j]) + cost
        childSubTreeRes[e][indexForAdjacents[node][j]] = result
        accum = max(accum, childSubTreeRes[node][j])
    nodeRes[node] = accum
ans = max(nodeRes)
print(ans)
