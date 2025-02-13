a, N = map(int, input().split())
from collections import deque, defaultdict

d = defaultdict(lambda: -1)
L = 1000000
q = deque([1])
d[1] = 0
while q:
    v = q.popleft()
    w = v * a
    # 操作1
    if w < L and d[w] == -1:
        d[w] = d[v] + 1
        q.append(w)
    # 操作2
    if v >= 10 and v % 10 != 0:
        mod = v % 10
        for i in range(1, 7):
            if v // 10 < pow(10, i):
                break
        x = pow(10, i) * mod + v // 10

        if x < L and d[x] == -1:
            d[x] = d[v] + 1
            q.append(x)
print(d[N])
