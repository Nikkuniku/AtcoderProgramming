A, X, M = map(int, input().split())
A_mat = [[A, 1], [0, 1]]


def mat_mul(a, b):
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= M
    return c


def pow_mat(A, n):
    p = [[0]*len(A) for _ in range(len(A))]

    # 基本行列にする
    for i in range(len(A)):
        p[i][i] = 1

    while n > 0:
        if n & 1:
            p = mat_mul(A, p)
        A = mat_mul(A, A)
        n >>= 1
    return p


A_mat = pow_mat(A_mat, X)
ans = A_mat[0][1]
print(ans)
