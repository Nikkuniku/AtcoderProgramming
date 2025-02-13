def solve(A, P):
    K = sum([(-2 + i) * A[i] for i in range(5)])
    if K >= 0:
        return 0
    if K % 2 == 0:
        res = min(P[3] * (-K), P[4] * ((-K + 1) // 2))
    else:
        res = min(P[3] * (-K), P[4] * (-K // 2) + P[3], P[4] * ((-K + 1) // 2))
    return res


def check(A, P, x, y):
    bunsi = A[0] + 2 * A[1] + 3 * A[2] + 4 * (A[3] + x) + 5 * (A[4] + y)
    bunbo = sum(A) + x + y
    if bunsi / bunbo >= 3:
        return P[3] * x + P[4] * y
    else:
        return 1 << 10


from random import random, randint

for _ in range(10):
    A = []
    P = []
    for _ in range(5):
        A.append(randint(5, 20))
    for _ in range(5):
        P.append(randint(5, 20))

    tmp = 1 << 60
    for i in range(100):
        for j in range(100):
            tmp = min(tmp, check(A, P, i, j))
    print(*A)
    print(*P)
    print(solve(A, P))
    print(tmp)
