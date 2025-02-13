N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
b = (K * K) // 2 + 1


def isOK(k):
    s = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            if A[i][j] >= k:
                s[i + 1][j + 1] = 1
    for i in range(N + 1):
        for j in range(N):
            s[i][j + 1] += s[i][j]
    for j in range(N + 1):
        for i in range(N):
            s[i + 1][j] += s[i][j]
    res = []
    for i in range(1, N - K + 1 + 1):
        if i + K - 1 > N:
            break
        for j in range(1, N - K + 1 + 1):
            if j + K - 1 > N:
                break
            tmp = (
                s[i + K - 1][j + K - 1]
                - s[i - 1][j + K - 1]
                - s[i + K - 1][j - 1]
                + s[i - 1][j - 1]
            )
            if tmp >= b:
                return True
    return False


l = -1
r = 1 << 30
while r - l > 1:
    mid = (l + r) // 2
    if isOK(mid):
        l = mid
    else:
        r = mid
print(l)
