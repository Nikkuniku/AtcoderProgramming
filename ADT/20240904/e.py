from heapq import heappop, heappush

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
q = []
for i in range(N):
    q.append((T[i], i))
INF = 1 << 60
ans = [INF] * N
while q:
    t, v = heappop(q)
    if t > ans[v]:
        continue
    ans[v] = t
    heappush(q, (t + S[v], (v + 1) % N))
print(*ans, sep="\n")
