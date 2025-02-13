from collections import defaultdict
import sys

sys.set_int_max_str_digits(0)
N = int(input())
d = defaultdict(list)
for _ in range(N):
    s = input()
    tmp = 0
    for i, v in enumerate(s):
        if v == "0":
            tmp += 1
        else:
            break
    d[int(s)].append((tmp, s))

Keys = sorted(d.keys())
ans = []
for k in Keys:
    A = sorted(d[k])[::-1]
    for _, a in A:
        ans.append(a)
print(*ans, sep="\n")
