def solve(n, k):
    s = 1 << (k - 1)
    res = [s]
    q = [s]
    i = k - 2
    while len(res) < n:
        if i < 0:
            break
        m = len(q)
        for j in range(m):
            q.append(q[j] + (1 << i))
            res.append(q[j] + (1 << i))
        i -= 1
    while len(res) < n:
        res.append(q[-1])
    while len(res) > n:
        res.pop()
    return res


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(*solve(N, K))
