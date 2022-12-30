from heapq import heappop, heappush
N, M = map(int, input().split())
maxA = 10**5 + 2
jobs = [[] for _ in range(maxA+1)]
for _ in range(N):
    a, b = map(int, input().split())
    jobs[a].append(b)
ans = 0
que = []
for i in range(M+1):
    for c in jobs[i]:
        heappush(que, -c)
    if que:
        ans += -heappop(que)

print(ans)
