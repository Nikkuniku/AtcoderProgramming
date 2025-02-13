from itertools import combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))
C = list(combinations(range(N), K))
MOD1 = 998
MOD2 = 998244353
ans = 0
for cmb in C:
    S_998 = 0
    S_998244353 = 0
    for i in cmb:
        S_998 += A[i]
        S_998244353 += A[i]
        S_998 %= MOD1
        S_998244353 %= MOD2
    ans += S_998244353 <= S_998
    ans %= MOD1

print(ans)
