from collections import Counter

S = input()
cnt = [0] * 101
C = Counter(S)
for k, v in C.items():
    cnt[v] += 1
ans = "Yes"
for p in cnt:
    if not (p == 0 or p == 2):
        ans = "No"
print(ans)
