from itertools import accumulate
from sortedcontainers import SortedList

N = int(input())
S = list(input())
T = list(input())
S_rev = S[::-1]
T_rev = T[::-1]
vs = [1 if s == "1" else 0 for s in S_rev]
vt = [1 if t == "1" else 0 for t in T_rev]
cs = list(accumulate(vs, initial=0))
ct = list(accumulate(vt, initial=0))
for i in range(N + 1):
    if cs[i] < ct[i]:
        exit(print(-1))
if cs[-1] % 2 != ct[-1] % 2:
    exit(print(-1))
SL = SortedList()
for i in range(N):
    if S[i] == "1":
        SL.add(i)
ans = 0
for i in range(N):
    if S[i] != T[i]:
        idx = SL.bisect_right(i)
        j = SL[idx]
        ans += j - i
        S[j] = "0"
        SL.discard(j)
    SL.discard(i)
print(ans)
