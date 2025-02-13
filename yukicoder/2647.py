from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


def solve(D, A, X):
    res = []
    for x in X:
        tmp = (2 * x + A) // (2 * A)
        res.append(tmp)
    return res


T = int(input())
ans = []
for _ in range(T):
    D, A = map(int, input().split())
    X = list(map(int, input().split()))
    ans.append(solve(D, A, X))
for c in ans:
    print(*c)
