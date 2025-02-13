from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
V = sorted(C.items())
L = 2 * 10**6 + 2
B = [0] * L
for k, e in V:
    j = k
    while k < L:
        B[k] += e
        k += j
ans = 0
for a in A:
    if B[a] > 1:
        continue
    ans += 1
print(ans)
