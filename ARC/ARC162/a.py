def solve(m, q):
    res = 0
    for i, v in enumerate(q):
        isOK = True
        for j in range(i+1, m):
            if v > q[j]:
                isOK = False
        if isOK:
            res += 1
    return res


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    ans.append(solve(N, P))
print(*ans, sep="\n")
