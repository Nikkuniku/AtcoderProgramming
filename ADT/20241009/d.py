from itertools import accumulate

S = "ABCDEFG"
d = [3, 1, 4, 1, 5, 9]
cum = list(accumulate(d, initial=0))
p, q = input().split()
if q < p:
    p, q = q, p
i = S.index(p)
j = S.index(q)
ans = cum[j] - cum[i]
print(ans)
