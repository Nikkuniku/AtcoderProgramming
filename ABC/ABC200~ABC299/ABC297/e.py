from heapq import heapify, heappush, heappop
from collections import defaultdict
N, K = map(int, input().split())
A = list(set(list(map(int, input().split()))))
A.sort()
d = defaultdict(lambda: -1)
hq = [0]
heapify(hq)
cnt = 0
while cnt <= K:
    v = heappop(hq)
    if d[v] != -1:
        continue
    d[v] = cnt
    cnt += 1
    for i in range(len(A)):
        heappush(hq, v+A[i])
print(v)
