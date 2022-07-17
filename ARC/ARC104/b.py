from collections import deque
from collections import Counter
n, s = input().split()
n = int(n)
AGCT = [0, 0, 0, 0]
d = {'A': 0, 'G': 1, 'C': 2, 'T': 3
     }
ans = 0
for i in range(1, n+1):
    if i % 2 == 1:
        continue
    q = deque()
    AGCT = [0, 0, 0, 0]
    j = 0
    while j < n:
        q.append(s[j])
        AGCT[d[s[j]]] += 1
        if len(q) == i:
            if AGCT[0] == AGCT[3] and AGCT[1] == AGCT[2]:
                ans += 1
            v = q.popleft()
            AGCT[d[v]] -= 1
        j += 1

print(ans)
