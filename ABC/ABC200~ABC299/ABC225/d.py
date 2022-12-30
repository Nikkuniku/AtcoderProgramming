from collections import deque
n, q = map(int, input().split())

mae = [-1]*(n+1)
child = [-1]*(n+1)
ans = []
for _ in range(q):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        t, x, y = query
        child[x] = y
        mae[y] = x
    elif query[0] == 2:
        t, x, y = query
        child[x] = -1
        mae[y] = -1
    else:
        t, x = query
        f = x
        b = x
        tmp = deque([x])

        while True:
            f = mae[f]
            if f == -1:
                break
            else:
                tmp.appendleft(f)
        while True:
            b = child[b]
            if b == -1:
                break
            else:
                tmp.append(b)
        ans.append(tmp)

for p in ans:
    print(len(p), *p)
