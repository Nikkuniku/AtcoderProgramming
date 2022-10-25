n = int(input())
MOD = 998244353
ans = 0


def cnt(k):
    return k//2


for q in range(1, n+1):
    if q**2 > n:
        break
    if q % 2 == 0:
        # pはq<=p<=N/qの範囲内で偶数のもの
        ans += cnt(n//q)-cnt(q-1)
        ans %= MOD
    else:
        ans += cnt((n//q)+1)-cnt(q-1)
        ans %= MOD
print(ans)
