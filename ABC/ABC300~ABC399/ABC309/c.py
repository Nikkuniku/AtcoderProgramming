from bisect import bisect_right
from itertools import accumulate
from collections import defaultdict
N, K = map(int, input().split())
med = defaultdict(lambda: 0)
total = 0
kouho = set([1])
for _ in range(N):
    a, b = map(int, input().split())
    med[a] += b
    kouho.add(a)
    kouho.add(a+1)
    total += b
Keys = sorted(med.keys())

Days = [1]
val = [0]
for c in Keys:
    Days.append(c)
    val.append(med[c])
CUM = list(accumulate(val))
kouho = sorted(list(kouho))
ans = -1
for c in kouho:
    idx = bisect_right(Days, c)
    tmp = total-CUM[idx-1]+med[c]
    if tmp <= K:
        ans = c
        break
print(ans)
