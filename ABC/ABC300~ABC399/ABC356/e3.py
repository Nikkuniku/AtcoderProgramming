from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
P = max(A)
C = [0] * (P + 1)
for a in A:
    C[a] += 1
cum = list(accumulate(C))
B = sorted(set(A))
ans = 0
for b in B:
    r = 2 * b - 1
    l = b - 1
    v = 1
    while v <= ((P + b - 1) // b):
        ans += v * (cum[min(r, P)] - cum[min(l, P)]) * C[b]
        v += 1
        r += b
        l += b
for c in C:
    ans -= c * (c - 1) // 2
ans -= sum(C)
print(ans)
