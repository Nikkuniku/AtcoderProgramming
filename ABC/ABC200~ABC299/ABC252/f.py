from heapq import heapify, heappop, heappush

N, L = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) < L:
    A.append(L - sum(A))
heapify(A)
ans = 0
while len(A) > 1:
    p = heappop(A)
    q = heappop(A)
    ans += p + q
    heappush(A, p + q)
if A[0] != L:
    ans += L
print(ans)
