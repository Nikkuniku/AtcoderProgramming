n = int(input())
m = 1000000007
a = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]


def mat_mul(a, b):
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= m
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


a = pow_mat(a, n-1)
ans = (2*a[2][0]+a[2][1]+a[2][2]) % m
print(ans)
