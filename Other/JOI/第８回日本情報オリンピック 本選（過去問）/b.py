from bisect import bisect_right
D = int(input())
N = int(input())
M = int(input())
dist = sorted([0]+[int(input()) for _ in range(N-1)]+[D])
K = [int(input()) for _ in range(M)]
ans = 0
for k in K:
    idx = bisect_right(dist, k)
    ans += min(k-dist[idx-1], dist[idx]-k)
print(ans)
