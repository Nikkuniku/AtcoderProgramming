from collections import Counter
s = input()

ans = -1
c = Counter(s)
for k, v in c.items():
    if v == 1:
        ans = k
print(ans)
