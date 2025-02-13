from collections import deque

N, Q = map(int, input().split())
front = [-1] * (N + 1)
back = [-1] * (N + 1)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1:]
        back[x] = y
        front[y] = x
    elif query[0] == 2:
        x, y = query[1:]
        back[x] = -1
        front[y] = -1
    elif query[0] == 3:
        x = query[1]
        res = deque([x])
        f = front[x]
        while f != -1:
            res.appendleft(f)
            f = front[f]
        b = back[x]
        while b != -1:
            res.append(b)
            b = back[b]
        print(len(res), *res)
