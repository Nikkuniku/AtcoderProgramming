from collections import defaultdict

N, Q = map(int, input().split())
pigeon = [i for i in range(N + 1)]
mapping = defaultdict(int)
root = [i for i in range(N + 1)]
for i in range(N + 1):
    mapping[i] = i
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1:]
        j = mapping[b]
        pigeon[a] = j
    elif query[0] == 2:
        a, b = query[1:]
        mapping[a], mapping[b] = mapping[b], mapping[a]
        root[mapping[a]] = a
        root[mapping[b]] = b
    elif query[0] == 3:
        a = query[1]
        ans.append(root[pigeon[a]])
print(*ans, sep="\n")
