from heapq import heappop, heappush

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
B = [[] for _ in range(N)]
for i in range(N):
    heappush(B[A[i] - 1], W[i])
ans = 0
for b in B:
    if not b:
        continue
    while len(b) > 1:
        v = heappop(b)
        ans += v
print(ans)
