from heapq import heapify, heappush, heappop
N = int(input())
A = list(map(int, input().split()))

hq1, hq2 = [], []
heapify(hq1)
heapify(hq2)
dp1 = [0]*(3*N)
dp2 = [0]*(3*N)
res = 0
for i in range(2*N):
    heappush(hq1, A[i])
    res += A[i]
    if len(hq1) > N:
        v = heappop(hq1)
        res -= v
    dp1[i] = res
res = 0
for j in range(3*N-1, N-1, -1):
    heappush(hq2, -A[j])
    res += A[j]
    if len(hq2) > N:
        v = heappop(hq2)
        res += v
    dp2[j] = res
ans = -(1 << 60)
for i in range(N-1, 2*N):
    ans = max(ans, dp1[i]-dp2[i+1])
print(ans)
