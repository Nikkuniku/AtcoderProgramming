from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = deque(A)
C = []
for i in range(K):
    C.append(B.popleft())
ans = B[-1] - B[0]
for i in range(K):
    B.pop()
    B.appendleft(C.pop())
    tmp = B[-1] - B[0]
    ans = min(ans, tmp)
print(ans)
