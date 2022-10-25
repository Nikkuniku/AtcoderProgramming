from itertools import groupby
s = input()

gr = groupby(s)
ans = 0
for k, v in gr:
    ans += 1
    print(k, list(v))
ans -= 1
print(ans)
