from collections import deque
Q = int(input())
que = deque()
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        x, c = query[1:]
        que.append((x, c))
    else:
        c = query[1]
        res = 0
        cnt = 0
        while cnt < c:
            y, p = que.popleft()
            cnt += p
            res += p*y
            if cnt-c > 0:
                que.appendleft((y, cnt-c))
                res -= (cnt-c)*y
        ans.append(res)
print(*ans, sep="\n")
