def solve(K, mod):
    res = 0
    M = int(K**0.5)
    res += pow(M, 3, MOD)
    tmp = 0
    for x in range(M+1, K+1):
        if K//x == 0:
            break
        tmp += (K//x)**2
        tmp %= mod
    res += 3*tmp
    res %= mod
    return res


MOD = 998244353
ans = []
T = int(input())
for _ in range(T):
    N = int(input())
    ans.append(solve(N, MOD))
print(*ans, sep="\n")
