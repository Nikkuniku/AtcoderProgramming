def solve(P):
    p1, p2, p3 = P
    if p1 > p2:
        p1, p2 = p2, p1
    if not (p3 == max(p1, p2) or p3 == max(p1, p2) + 1):
        return 0
    MOD = 998244353
    ans = 9 * pow(10, p1 - 1, MOD) * 9 * pow(10, p2 - 1, MOD)
    ans %= MOD
    ans -= 45 * pow(10, p1 - 1, MOD)
    ans %= MOD
    return ans


T = int(input())
ans = []
for _ in range(T):
    A = list(map(int, input().split()))
    ans.append(solve(A))
print(*ans, sep="\n")
