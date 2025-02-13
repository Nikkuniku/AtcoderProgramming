S = input()
from collections import Counter

C = Counter(S)
N = len(S)
ans = N * (N - 1) // 2
add = False
for k, v in C.items():
    if v >= 2:
        add = True
    ans -= v * (v - 1) // 2
if add:
    ans += 1
print(ans)
