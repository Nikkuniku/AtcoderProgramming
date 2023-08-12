
from math import factorial
from collections import Counter


def nCr(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))


N, A, B = map(int, input().split())
V = sorted(list(map(int, input().split())))[::-1]
C = Counter(V)
a = []
for i in range(A):
    a.append(V[i])
M = sum(a)/len(a)


def Count(Q):
    res = 1
    C_tmp = Counter(Q)
    for k, v in C_tmp.items():
        res *= nCr(C[k], C_tmp[k])
    return res


ans = Count(a)
for i in range(A, B):
    p = V[i]
    if sum(a) == len(a)*p:
        a.append(p)
        ans += Count(a)
print(M)
print(ans)
