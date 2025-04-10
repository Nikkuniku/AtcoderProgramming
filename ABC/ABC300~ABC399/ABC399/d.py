from collections import defaultdict


def solve(N, A):
    nomove = [False] * (2 * N)
    d = defaultdict(list)
    for i in range(2 * N - 1):
        if A[i] == A[i + 1]:
            nomove[i] = nomove[i + 1] = True
    for i in range(2 * N - 1):
        if nomove[i] or nomove[i + 1]:
            continue
        a = A[i]
        b = A[i + 1]
        if b < a:
            a, b = b, a
        d[(a, b)].append((i, i + 1))
    res = 0
    for key, value in d.items():
        temp = set()
        for p, q in value:
            temp.add(p)
            temp.add(q)
        res += len(temp) == 4

    return res


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    ans.append(res)
print(*ans, sep="\n")
