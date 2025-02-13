def matrix_rotate(A: list) -> list:
    """
    2次元リストの180度回転
    Parameters
    ----------
    A:any[][]
    """
    return [A[i][::-1] for i in range(len(A))][::-1]


def matrix_transpose(A: list) -> list:
    """
    2次元リストの転置
    Parameters
    ----------
    A:any[][]
    """
    return [list(x) for x in zip(*A)]


def matrix_rotate90degree_toright(A: list) -> list:
    """
    2次元リストの90度右回転
    Parameters
    ----------
    A:any[][]
    """
    return [list(x) for x in zip(*A[::-1])]


def matrix_rotate90degree_toleft(A: list) -> list:
    """
    2次元リストの90度左書回転
    Parameters
    ----------
    A:any[][]
    """
    return [list(x) for x in zip(*A)][::-1]


A = [[1, 2, 3], [4, 5, 6]]
print(*matrix_rotate(A), sep="\n")
print(*matrix_transpose(A), sep="\n")
print(*matrix_rotate90degree_toright(A), sep="\n")
print(*matrix_rotate90degree_toleft(A), sep="\n")
