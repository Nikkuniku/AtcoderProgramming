def make_array(k):
    from random import randint

    A = [randint(-100, 100) for _ in range(k)]
    return A


def check(A):
    from itertools import combinations, pairwise

    M = len(A)
    C = combinations([i for i in range(M)], M // 2)
    res = -(1 << 60)
    p = -1
    for c in C:
        tmp = 0
        isOK = True
        for a, b in pairwise(c):
            if abs(a - b) <= 1:
                isOK = False
                break
            tmp += A[a]
        tmp += A[c[-1]]
        if isOK:
            if res < tmp:
                res = tmp
                p = c
    return res, p


def solve(A):
    N = len(A)
    M = N // 2
    INF = 1 << 60
    dp = [[-INF] * 2 for _ in range(M + 1)]
    dp[0] = [0, 0]
    if N % 2 == 0:
        for i in range(N):
            k = i // 2
            if i % 2 == 0:
                dp[k + 1][0] = dp[k][0] + A[i]
            else:
                dp[k + 1][1] = max(dp[k][0], dp[k][1]) + A[i]
        ans = max(dp[M])
    else:
        for i in range(N - 1):
            k = i // 2
            if i % 2 == 0:
                dp[k + 1][0] = dp[k][0] + A[i]
            else:
                dp[k + 1][1] = max(dp[k]) + A[i]
        B = A[::-1]
        ep = [[-INF] * 2 for _ in range(M + 1)]
        ep[0] = [0, 0]
        for i in range(N - 1):
            k = i // 2
            if i % 2 == 0:
                ep[k + 1][0] = ep[k][0] + B[i]
            else:
                ep[k + 1][1] = max(ep[k]) + B[i]
        ep = ep[::-1]
        ans = max(max(dp[-1]), max(ep[0]))
        for j in range(1, N, 2):
            p = j // 2
            q = (j // 2) + 1
            ans = max(ans, dp[p][0] + A[j - 1] + max(ep[q]))
            ans = max(ans, max(dp[p]) + A[j] + max(ep[q]))
            ans = max(ans, max(dp[p]) + A[j + 1] + ep[q][0])
    return ans


N = int(input())
for _ in range(20):
    A = make_array(N)
    tmp1, P = check(A)
    tmp2 = solve(A)
    if tmp1 != tmp2:
        print(A)
        print(tmp1, P)
        print(tmp2)
