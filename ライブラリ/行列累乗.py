def mat_mul(a, b):
    """
    a: 行列(2次元配列)I*J
    b: 行列(2次元配列)J*K
    """
    MOD = 1000000007
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= MOD
    return c


def pow_mat(A, n):
    """
    A: 正方行列(2次元配列)
    n: 累乗指数
    """
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


n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

a = pow_mat(a, k)
ans = 0
for i in range(n):
    for j in range(n):
        ans += a[i][j]
print(ans)
