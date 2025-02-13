N, M = map(int, input().split())
X = list(map(int, input().split()))
R = [0] * (N + 2)
for i in range(M - 1):
    p = X[i]
    q = X[i + 1]
    if p > q:
        p, q = q, p
    tmp = q - p
    tmp_rev = N - (q - p)
    R[p] += tmp_rev
    R[q] -= tmp_rev
    R[q] += tmp
    R[N + 1] -= tmp
    R[1] += tmp
    R[p] -= tmp
for i in range(N + 1):
    R[i + 1] += R[i]
ans = min(R[1 : N + 1])
print(ans)
