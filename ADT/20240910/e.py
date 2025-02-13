from collections import Counter

S = input()
C = Counter(S)
N = len(S)
ans = N * (N - 1) // 2
isOK = 0
for v in C.values():
    ans -= v * (v - 1) // 2
    if v > 1:
        isOK = 1
ans += isOK
print(ans)
