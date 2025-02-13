def rangesum(l, r):
    res = r * (r + 1) // 2
    res -= l * (l - 1) // 2
    return res


N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [(X[i], A[i]) for i in range(M)]
B.sort()
X = [B[i][0] for i in range(M)]
A = [B[i][1] for i in range(M)]
if X[0] != 1 or sum(A) != N:
    exit(print(-1))
ans = 0
blank = N
for i in range(M - 1, -1, -1):
    K = blank - X[i]
    if A[i] > K + 1:
        ans = -1
        break
    if i > 0:
        ans += rangesum(K - (A[i] - 1), K)
        blank = blank - A[i]
    else:
        if A[0] - 1 == K:
            ans += rangesum(1, K)
        else:
            ans = -1
print(ans)
