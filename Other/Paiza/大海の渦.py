from collections import deque
n, x1 = map(int, input().split())
d = list(map(int, input().split()))

q = deque()
ans = []
tmp = 0
for i in range(n):
    if i == 0:
        ans.append(x1)
        tmp += x1
        q.append(x1)
    else:
        x = d[i-1]-tmp
        tmp += x
        ans.append(x)
        q.append(x)
        if len(q) == 3:
            tmp -= q.popleft()
print(*ans)
