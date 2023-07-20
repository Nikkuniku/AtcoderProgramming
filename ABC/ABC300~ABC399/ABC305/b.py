from itertools import accumulate
from string import ascii_uppercase
p, q = input().split()

P = [0, 3, 1, 4, 1, 5, 9]
ac = list(accumulate(P))
i = ascii_uppercase.index(p)
j = ascii_uppercase.index(q)
ans = abs(ac[i]-ac[j])
print(ans)
