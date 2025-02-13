def mat_mul(a, b):
    """
    a: 行列(2次元配列)I*J
    b: 行列(2次元配列)J*K
    """
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k] * b[k][j]
    return c


def pow_mat(A, n):
    """
    A: 正方行列(2次元配列)
    n: 累乗指数
    """
    p = [[0] * len(A) for _ in range(len(A))]

    # 基本行列にする
    for i in range(len(A)):
        p[i][i] = 1

    while n > 0:
        if n & 1:
            p = mat_mul(A, p)
        A = mat_mul(A, A)
        n >>= 1
    return p


def solve():
    mat = [[1, 1], [1, 0]]
    r = 10000
    l = 3
    while r - l > 1:
        mid = (l + r) // 2
        M = pow_mat(mat, mid - 2)
        fib = sum(M[0])
        if len(str(fib)) >= 1000:
            r = mid
        else:
            l = mid
    print(r)
    a = sum(pow_mat(mat, r - 2)[0])
    b = sum(pow_mat(mat, r - 1 - 2)[0])
    print(len(str(a)))
    print(len(str(b)))


import time

start = time.time()  # 現在時刻（処理開始前）を取得

# 実行したい処理を記述
solve()

end = time.time()  # 現在時刻（処理完了後）を取得

time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print(time_diff)  # 処理にかかった時間データを使用
