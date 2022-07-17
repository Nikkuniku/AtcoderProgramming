from collections import defaultdict, deque
n = int(input())
s = []
for _ in range(2):
    s.append(list(input()))

v = 0
d = defaultdict(int)
for i in range(n):
    for j in range(2):
        if s[j][i] not in d:
            d[s[j][i]] = v
            v += 1

dx = [1, 0]
dy = [0, 1]
edge = [set() for _ in range(v)]
for i in range(n):
    for j in range(2):
        p = d[s[j][i]]
        for k in range(2):
            if j+dx[k] < 2 and i+dy[k] < n:
                q = d[s[j+dx[k]][i+dy[k]]]
                if p != q:
                    edge[p].add(q)
                    edge[q].add(p)

for i in range(v):
    edge[i] = list(edge[i])
seen = [False]*v
q = deque([0])
colors = [3]*v
while q:
    v = q.popleft()
    if seen[v]:
        continue
    seen[v] = True
    for e in edge[v]:
        if seen[e]:
            continue
        colors[e] -= 1
        q.append(e)
ans = 1
MOD = 1000000007
for c in colors:
    ans *= c
    ans %= MOD
print(ans)
