def solve(n, x):
    if n * (n + 1) // 2 > x:
        return [-1]
    res = []
    tmp = 0
    for i in range(1, n):
        res.append(i)
        tmp += i
    res.append(x - tmp)
    return res


T = int(input())
ans = []
for _ in range(T):
    N, X = map(int, input().split())
    ans.append(solve(N, X))
for c in ans:
    print(*c)
