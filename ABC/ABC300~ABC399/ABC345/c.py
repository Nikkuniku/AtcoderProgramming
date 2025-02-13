from collections import Counter

S = input()
N = len(S)
C = Counter(S)
ans = N * (N - 1) // 2
for k, v in C.items():
    ans -= v * (v - 1) // 2
if max(C.values()) > 1:
    ans += 1
print(ans)
