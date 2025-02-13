from collections import Counter

S = input()
C = Counter(S)
N = len(S)
ans = "Yes"
for i in range(1, N + 1):
    tmp = set()
    for k, v in C.items():
        if v == i:
            tmp.add(k)
    if not (len(tmp) == 0 or len(tmp) == 2):
        ans = "No"
print(ans)
