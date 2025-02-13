N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def f(A):
    M = len(A)
    top = -1
    left = -1
    for i in range(M):
        for j in range(M):
            if A[i][j] == "#":
                top = i
                break
        if top != -1:
            break
    for j in range(M):
        for i in range(M):
            if A[i][j] == "#":
                left = j
                break
        if left != -1:
            break
    B = [["."] * M for _ in range(M)]
    for i in range(top, M):
        for j in range(left, M):
            B[i - top][j - left] = A[i][j]

    return B


def matrix_rotate90degree_toright(A: list) -> list:
    """
    2次元リストの90度右回転
    Parameters
    ----------
    A:any[][]
    """
    return [list(x) for x in zip(*A[::-1])]


ans = "No"
for _ in range(4):
    S = matrix_rotate90degree_toright(S)
    for _ in range(4):
        T = matrix_rotate90degree_toright(T)
        if f(S) == f(T):
            ans = "Yes"
            break
print(ans)
