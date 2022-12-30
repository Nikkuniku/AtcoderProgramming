N = int(input())
M = int(input())
MOD = 998244353


def modinv(x):
    return pow(x, MOD-2, MOD)


ans = pow(2, N, MOD)

tmp = 1
for m in range(M):
    if N >= m:
        if m == 0:
            ans -= 1
        else:
            tmp *= (N-(m-1))
            tmp *= modinv(m)
            tmp %= MOD
            ans -= tmp
    ans %= MOD
print(ans)
