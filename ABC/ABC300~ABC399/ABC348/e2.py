N = int(input())
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
C = list(map(int, input().split()))
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
    # 値の累積
    result_a = 0
    # nodeを根とする部分木の値の和
    result_b = C[node]
    parentIndex = -1
    for j in range(len(adjacents[node])):
        if adjacents[node][j] == parent:
            parentIndex = j
            continue
        result_a += childSubTreeRes[node][j][0] + childSubTreeRes[node][j][1]
        result_b += childSubTreeRes[node][j][1]
    if leaf[node]:
        childSubTreeRes[parent][indexForAdjacents[node][parentIndex]][0] = result_a
        childSubTreeRes[parent][indexForAdjacents[node][parentIndex]][1] = result_b
    else:
        childSubTreeRes[parent][indexForAdjacents[node][parentIndex]][0] = result_a
        childSubTreeRes[parent][indexForAdjacents[node][parentIndex]][1] = result_b
for i in range(len(order)):
    node = order[i]
    accumsFromTail = [[0, 0] for _ in range(len(adjacents[node]))]
    for j in range(len(accumsFromTail) - 1, 0, -1):
        accumsFromTail[j - 1][0] = (
            childSubTreeRes[node][j][0]
            + childSubTreeRes[node][j][1]
            + accumsFromTail[j][0]
        )
        accumsFromTail[j - 1][1] = childSubTreeRes[node][j][1] + accumsFromTail[j][1]
    accum_a = 0
    accum_b = C[node]
    for j in range(len(accumsFromTail)):
        e = adjacents[node][j]
        result_a = accum_a + accumsFromTail[j][0]
        result_b = accum_b + accumsFromTail[j][1]
        childSubTreeRes[e][indexForAdjacents[node][j]][0] = result_a
        childSubTreeRes[e][indexForAdjacents[node][j]][1] = result_b
        accum_a = accum_a + childSubTreeRes[node][j][0] + childSubTreeRes[node][j][1]
        accum_b = accum_b + childSubTreeRes[node][j][1]
    nodeRes[node] = accum_a
print(min(nodeRes))
