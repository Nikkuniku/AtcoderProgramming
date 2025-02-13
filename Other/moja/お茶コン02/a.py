def solve(M, D, N):
    res = (M - 1 + (N - 1) * D) % 12 + 1
    return res


T = int(input())
ans = []
for _ in range(T):
    n, m, d = map(int, input().split())
    ans.append(solve(n, m, d))
print(*ans, sep="\n")
