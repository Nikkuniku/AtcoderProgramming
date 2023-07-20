from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))
p = A[0]
q = A[1]
B = []
cnt = 0
for i in range(2, N):
    if p <= A[i] <= q:
        cnt += 1
    else:
        if A[i] < p or q < A[i]:
            B.append(A[i])
B.sort()
ans = 1 << 60 if cnt < M else 0
if cnt < M:
    C = deque()
    for i in range(len(B)):
        C.append(B[i])
        if len(C) == M-cnt:
            L = C[0]
            R = C[-1]
            ans = min(ans, max(p-L, 0)+max(R-q, 0))
            C.popleft()
print(ans)
