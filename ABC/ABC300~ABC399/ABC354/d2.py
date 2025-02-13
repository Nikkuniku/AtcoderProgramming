A, B, C, D = map(int, input().split())
A += 10**9
B += 10**9
C += 10**9
D += 10**9


def f(X, Y):
    H = [[2, 1, 0, 1], [1, 2, 1, 0]]
    res = 0
    res += sum(H[0]) * (X // 4) * ((Y + 1) // 2)
    res += sum(H[1]) * (X // 4) * (Y // 2)

    res += sum(H[0][: X % 4]) * ((Y + 1) // 2)
    res += sum(H[1][: X % 4]) * (Y // 2)

    return res


ans = f(C, D) - f(C, B) - f(A, D) + f(A, B)
print(ans)
