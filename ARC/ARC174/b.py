def solve(A, P):
    K = sum([(-2 + i) * A[i] for i in range(5)])
    if K >= 0:
        return 0
    if K % 2 == 0:
        res = min(P[3] * (-K), P[4] * ((-K + 1) // 2))
    else:
        res = min(P[3] * (-K), P[4] * (-K // 2) + P[3], P[4] * ((-K + 1) // 2))
    return res


T = int(input())
ans = []
for _ in range(T):
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    ans.append(solve(A, P))
print(*ans, sep="\n")
