from collections import Counter

S = input()
if len(S) % 2 != 0:
    exit(print("No"))
ans = "Yes"
for i in range(len(S) // 2):
    if S[2 * i] != S[2 * i + 1]:
        ans = "No"
        break
C = Counter(S)
Vals = C.values()
if not (min(Vals) == max(Vals) == 2):
    ans = "No"
print(ans)
