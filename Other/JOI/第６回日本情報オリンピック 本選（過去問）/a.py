from collections import deque
N, K = map(int, input().split())
q = deque()
ans = -(1 << 60)
tmp = 0
for i in range(N):
    a = int(input())
    q.append(a)
    tmp += a
    if len(q) == K:
        ans = max(ans, tmp)
        tmp -= q.popleft()
print(ans)
