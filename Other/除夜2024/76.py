from heapq import heappop, heappush

N = int(input())
Box = [[] for _ in range(N)]
A = list(map(int, input().split()))
W = list(map(int, input().split()))
ans = 0
for i in range(N):
    heappush(Box[A[i] - 1], W[i])
for i in range(N):
    while len(Box[i]) > 1:
        p = heappop(Box[i])
        ans += p
print(ans)
