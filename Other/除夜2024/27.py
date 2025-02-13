from collections import Counter

A = list(map(int, input().split()))
C = Counter(A)
ans = 0
for k, v in C.items():
    ans += v // 2
print(ans)
