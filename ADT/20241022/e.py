N = int(input())
ans = 0
MOD = 998244353


def calc(m):
    return m * (m + 1) // 2


for k in range(1, 19):
    p = pow(10, k - 1)
    q = pow(10, k) - 1
    if p <= N:
        ans += calc(min(q, N) - p + 1)
        ans %= MOD
print(ans)
