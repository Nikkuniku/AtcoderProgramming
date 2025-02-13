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
            p = (j - 1) // 2
            q = (j + 1) // 2
            ans = max(ans, dp[p][0] + A[j - 1] + max(ep[q]))
            ans = max(ans, max(dp[p]) + A[j] + max(ep[q]))
            ans = max(ans, max(dp[p]) + A[j + 1] + ep[q][0])
    return ans


N = int(input())
A = list(map(int, input().split()))
print(solve(A))
