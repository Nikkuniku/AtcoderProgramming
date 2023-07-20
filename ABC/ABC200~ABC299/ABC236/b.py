from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
ans = -1
for k, v in C.items():
    if v != 4:
        ans = k
print(ans)
