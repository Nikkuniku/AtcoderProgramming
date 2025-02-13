def matrix_rotate90degree_toright(A: list) -> list:
    """
    2次元リストの90度右回転
    Parameters
    ----------
    A:any[][]
    """
    return [list(x) for x in zip(*A[::-1])]


N = int(input())
S = [list(input()) for _ in range(N)]

ans = matrix_rotate90degree_toright(S)
for c in ans:
    print(*c, sep="")
