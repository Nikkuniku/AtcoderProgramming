from collections import Counter

A = list(map(int, input().split()))
C = Counter(A)
ans = 0
for i, v in C.most_common():
    ans += v // 2
print(ans)
