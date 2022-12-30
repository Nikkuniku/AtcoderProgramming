from collections import deque
a, N = map(int, input().split())

dist = [-1]*pow(10,6)
q = deque([1])
dist[1] = 0
while q:
    v = q.popleft()

    # 操作1
    p=a*v
    if p < pow(10,6) and dist[p] == -1:
        q.append(p)
        dist[p] = dist[v]+1

    # 操作2
    if v >= 10 and v % 10 != 0:
        le = len(str(v))
        k = v % 10
        w = pow(10, le-1)*k+(v//10)
        if w < pow(10,6) and dist[w] == -1:
            q.append(w)
            dist[w] = dist[v]+1
print(dist[N])
