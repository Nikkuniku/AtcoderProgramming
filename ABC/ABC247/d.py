from collections import deque
Q = int(input())
d = deque()
ans = []
for _ in range(Q):
    query = tuple(map(int, input().split()))
    q = query[0]

    if q == 1:
        x = query[1]
        c = query[2]

        if d:
            if d[-1][0] == x:
                d[-1][1] += c
        d.append([x, c])
    else:
        c = query[1]
        tmp = 0
        while d:
            v = d[0][1]
            if v > c:
                d[0][1] -= c
                tmp += d[0][0]*c
                break
            else:
                v = d.popleft()
                tmp += v[0]*v[1]
                c -= v[1]
        ans.append(tmp)
print(*ans, sep="\n")
