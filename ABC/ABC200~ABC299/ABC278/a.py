from collections import deque
N, K = map(int, input().split())
a = list(map(int, input().split()))
q = deque(a)
for _ in range(K):
    q.popleft()
    q.append(0)

print(*q)
