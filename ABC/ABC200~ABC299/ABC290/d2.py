
from math import gcd, ceil


def solve(n, d, k):
    g = gcd(n, d)
    if n == d:
        return k-1
    if g == 1:
        return (k-1)*d % n
    else:
        M = n//g
        F = d//g
        L = M
        c = ceil(k/L)-1
        k %= L
        res = (k-1)*d % n
        res += c

        return res


T = int(input())
ans = []
for _ in range(T):
    N, D, K = map(int, input().split())
    ans.append(solve(N, D, K))
print(*ans, sep="\n")
