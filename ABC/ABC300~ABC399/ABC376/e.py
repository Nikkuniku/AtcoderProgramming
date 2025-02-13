from sortedcontainers import SortedList


def solve(N, K, A, B):
    C = [(A[i], B[i]) for i in range(N)]
    C.sort()
    S = SortedList()
    res = 0
    b_sum = 0
    for i in range(K):
        a = C[i][0]
        b_sum += C[i][1]
        S.add(C[i][1])
    res = a * b_sum
    for i in range(K, N):
        a = C[i][0]
        b_sum += C[i][1] - S.pop()
        S.add(C[i][1])
        res = min(res, a * b_sum)
    return res


T = int(input())
ans = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans.append(solve(N, K, A, B))
print(*ans, sep="\n")
