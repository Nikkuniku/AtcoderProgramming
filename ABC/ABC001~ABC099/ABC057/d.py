
from math import factorial
from collections import Counter


def nCr(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))


N, A, B = map(int, input().split())
V = list(map(int, input().split()))
V.sort(reverse=True)
C = Counter(V)
a = []
for i in range(A):
    a.append(V[i])
p = a[-1]
ans = sum(a)/len(a)
print(ans)

ans2 = nCr(C[p], a.count(p))
for i in range(A+1, B):
    if ans == (ans+V[i])/(len(a)+1):
        a.append(V[i])
        p = a[-1]
        ans2 += nCr(C[p], a.count(p))
print(ans2)
