N, M = map(int, input().split())


def solve2(N, M):
    ans = 0
    MOD = 998244353
    for i in range(61):
        if M & (1 << i) == 0:
            continue
        ans += pow(2, i, MOD) * ((N + 1) // pow(2, i + 1))
        k = max(((N + 1) % pow(2, i + 1)) - pow(2, i), 0)
        ans += k
        ans %= MOD
    return ans


print(solve2(N, M))
