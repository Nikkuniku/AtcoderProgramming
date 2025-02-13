from collections import defaultdict

S = input()[::-1]
P = 2019
d = defaultdict(int)
d[0] = 1
cum = 0
ans = 0
for s in S:
    cum = (10 * cum + int(s)) % P
    ans += d[cum]
    d[cum] += 1
print(ans)
