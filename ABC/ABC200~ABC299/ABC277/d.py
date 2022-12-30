from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
S = sum(a)
b = a+a
ans = 1 << 62
q = deque()
res = 0
pre = b[0]
for c in b:
    q.append(c)
    res += c
    while len(q) > 1 and not(c == pre or c == (pre+1) % m):
        v = q.popleft()
        res -= v
    pre = c
    ans = min(ans, S-min(res, S))


print(ans)
