from collections import Counter

N = int(input())
A = list(map(int, input().split()))
xorsum = 0
for a in A:
    xorsum ^= a
if xorsum:
    exit(print(-1))
C = Counter(A)
if all([v % 2 == 0 for v in C.values()]):
    exit(print(0))
maxA = 0
for k, v in C.items():
    if v % 2 != 0:
        maxA = max(maxA, k)
print(maxA - 1)
