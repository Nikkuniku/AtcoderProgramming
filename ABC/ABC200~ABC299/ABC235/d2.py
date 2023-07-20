from collections import defaultdict, deque
a, N = map(int, input().split())
q = deque([1])
dist = defaultdict(lambda: -1)
dist[1] = 0
lim = 10**6
while q:
    v = q.popleft()
    if dist[a*v] == -1:
        dist[a*v] = dist[v]+1
        if a*v < lim:
            q.append(a*v)
    if v >= 10 and v % 10 != 0:
        w = int(str(v)[-1]+str(v)[:len(str(v))-1])
        if dist[w] == -1:
            dist[w] = dist[v]+1
            if w < lim:
                q.append(w)
print(dist[N])
