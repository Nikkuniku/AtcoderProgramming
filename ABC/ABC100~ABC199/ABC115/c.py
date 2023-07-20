from collections import deque
N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()
ans = 1 << 60
q = deque()
for i in range(N):
    q.append(H[i])
    if len(q) == K:
        ans = min(ans, q[-1]-q[0])
        q.popleft()
print(ans)
