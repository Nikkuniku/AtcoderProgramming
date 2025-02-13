from collections import Counter

S = input()
C = Counter(S)
v = C.most_common()[0][1]
ans = []
for k, w in C.items():
    if w == v:
        ans.append(k)
ans.sort()
print(ans[0])
