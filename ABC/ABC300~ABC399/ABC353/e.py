from collections import defaultdict

N = int(input())
S = list(input().split())

next = defaultdict(lambda: -1)
Trie = defaultdict(int)
Nodes = 1
ans = 0
for s in S:
    node_id = 0
    for i, si in enumerate(s):
        next_id = next[node_id, si]
        if next_id == -1:
            next_id += Nodes + 1
            Nodes += 1
            next[node_id, si] = next_id
        else:
            ans += Trie[next_id]
        node_id = next_id
        Trie[node_id] += 1
print(ans)
