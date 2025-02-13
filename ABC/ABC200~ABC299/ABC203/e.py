N, M = map(int, input().split())
from collections import defaultdict, deque
from bisect import bisect_right

dist = defaultdict(lambda: -1)
col = defaultdict(list)
col[N].append(0)
q = deque([(0, N)])
for _ in range(M):
    x, y = map(int, input().split())
    col[y].append(x)
for key in col.keys():
    col[key].sort()
dist[(0, N)] = 0
while q:
    i, j = q.popleft()
    idx = bisect_right(col[j], i)
    if idx == len(col[j]):
        k = 2 * N
    else:
        k = col[j][idx]
    for nextj in [j - 1, j + 1]:
        start = bisect_right(col[nextj], i)
        last = bisect_right(col[nextj], k)
        for p in range(start, last):
            nexti = col[nextj][p]
            if dist[(nexti, nextj)] == -1:
                dist[(nexti, nextj)] = dist[(i, j)] + 1
                q.append((nexti, nextj))
ans = 0
for j in col.keys():
    if not col[j]:
        continue
    i = col[j][-1]
    ans += dist[(i, j)] >= 0
print(ans)
