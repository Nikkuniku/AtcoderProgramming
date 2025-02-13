from collections import Counter

N = int(input())
D = list(map(int, input().split()))
MOD = 998244353
C = Counter(D)
if D[0] > 0:
    exit(print(0))
ans = 1
values = [(k, v) for k, v in C.items()]
values.sort()
for k, v in values:
    if k == 0:
        if v > 1:
            exit(print(0))
    else:
        if C[k - 1] == 0:
            exit(print(0))
        tmp = pow(C[k - 1], C[k], MOD)
        ans *= tmp
        ans %= MOD
print(ans)
