from collections import Counter

S = list(input())
C = Counter(S)
a = C.most_common()
M = max(C.values())
b = []
for k, v in a:
    if v == M:
        b.append(k)
b.sort()
print(b[0])
