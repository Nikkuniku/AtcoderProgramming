N, M = map(int, input().split())
adjacents = [[] for _ in range(N)]
indexForAdjacents = [[] for _ in range(N)]
for _ in range(N - 1):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    indexForAdjacents[s].append(len(adjacents[t]))
    indexForAdjacents[t].append(len(adjacents[s]))
    adjacents[s].append(t)
    adjacents[t].append(s)
childSubTreeRes = [[[0, 0] for _ in range(len(adjacents[i]))] for i in range(N)]
nodeRes = [0] * N
parents = [-1] * N
order = []
stack = [0]
leaf = [False] * N
while stack:
    node = stack.pop()
    order.append(node)
    isleaf = True
    for e in adjacents[node]:
        if e == parents[node]:
            continue
        stack.append(e)
        parents[e] = node
        isleaf = False
    leaf[node] = isleaf
for i in range(len(order) - 1, 0, -1):
    node = order[i]
    parent = parents[node]
    a, b = 1, 1
    parentIndex = -1
    for j in range(len(adjacents[node])):
        if adjacents[node][j] == parent:
            parentIndex = j
            continue
        a *= childSubTreeRes[node][j][0]
        b *= sum(childSubTreeRes[node][j])
        a %= M
        b %= M
    if leaf[node]:
        childSubTreeRes[parent][indexForAdjacents[node][parentIndex]][0] = 1
        childSubTreeRes[parent][indexForAdjacents[node][parentIndex]][1] = 1
    else:
        childSubTreeRes[parent][indexForAdjacents[node][parentIndex]][0] = a
        childSubTreeRes[parent][indexForAdjacents[node][parentIndex]][1] = b
for i in range(len(order)):
    node = order[i]
    accumsFromTail = [[1, 1] for _ in range(len(adjacents[node]))]
    for j in range(len(accumsFromTail) - 1, 0, -1):
        accumsFromTail[j - 1][0] = childSubTreeRes[node][j][0] * accumsFromTail[j][0]
        accumsFromTail[j - 1][1] = sum(childSubTreeRes[node][j]) * accumsFromTail[j][1]
        accumsFromTail[j - 1][0] %= M
        accumsFromTail[j - 1][1] %= M
    accum_a = 1
    accum_b = 1
    for j in range(len(accumsFromTail)):
        e = adjacents[node][j]
        result_a = accum_a * accumsFromTail[j][0]
        result_b = accum_b * accumsFromTail[j][1]
        childSubTreeRes[e][indexForAdjacents[node][j]][0] = result_a
        childSubTreeRes[e][indexForAdjacents[node][j]][1] = result_b
        accum_a = accum_a * childSubTreeRes[node][j][0] % M
        accum_b = accum_b * sum(childSubTreeRes[node][j]) % M
    nodeRes[node] = accum_b % M
print(*nodeRes, sep="\n")
