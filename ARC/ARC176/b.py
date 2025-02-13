def solve(n, m, k):
    if m == k + 1 and k == n:
        return 0
    if n >= m:
        p = (n - m + 1 + m - k - 1) // (m - k)
        n -= p * (m - k)
        if m == k + 1 and k == n:
            return 0
    return pow(2, n, 10)


T = int(input())
ans = []
for _ in range(T):
    N, M, K = map(int, input().split())
    ans.append(solve(N, M, K))
print(*ans, sep="\n")
