MOD = 998244353


def powten(k):
    return pow(10, k, MOD)


inv = pow(2, -1, MOD)


def solve(a1, a2, a3):
    if a1 > a2:
        a1, a2 = a2, a1
    if a3 != a2 and a3 != a2 + 1:
        return 0
    if a2 == a3:
        if a1 == a2:
            return 4 * powten(a2 - 1) * (8 * powten(a2 - 1) + 1) % MOD
        else:
            return (
                9
                * powten(a1 - 1)
                * ((9 * powten(a2 - 1)) - (powten(a1 - 1) + powten(a1) - 1) * inv)
            ) % MOD
    else:
        ans = 81 * powten(a1 + a2 - 2)
        if a1 == a2:
            ans -= 4 * powten(a2 - 1) * (8 * powten(a2 - 1) + 1) % MOD
        else:
            ans -= (
                9
                * powten(a1 - 1)
                * ((9 * powten(a2 - 1)) - (powten(a1 - 1) + powten(a1) - 1) * inv)
            )
        ans %= MOD
        return ans


T = int(input())
ans = []
for _ in range(T):
    A = list(map(int, input().split()))
    ans.append(solve(*A))
print(*ans, sep="\n")
