
from collections import deque
n = int(input())
a = list(map(int, input().split()))
a.sort()
q = deque(a)
ans = 0
while len(q) > 1:
    L = q.popleft()
    R = q.pop()
    if R % L != 0:
        q.appendleft(L)
        q.appendleft(R % L)
    else:
        q.appendleft(L)
    ans += 1
print(ans)
