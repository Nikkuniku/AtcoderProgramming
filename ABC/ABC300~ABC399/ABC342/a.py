from collections import Counter

S = list(input())
C = Counter(S)
t = ""
for k, v in C.items():
    if v == 1:
        t = k
ans = -1
for i in range(len(S)):
    if S[i] == t:
        ans = i
        break
print(ans + 1)
