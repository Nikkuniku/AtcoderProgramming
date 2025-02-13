def matrix_rotate90degree_toright(A: list) -> list:
    """
    2次元リストの90度右回転
    Parameters
    ----------
    A:any[][]
    """
    return [list(x) for x in zip(*A[::-1])]


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
ans = "No"
for _ in range(4):
    A = matrix_rotate90degree_toright(A)
    isOK = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] != 1:
                isOK = False
    if isOK:
        ans = "Yes"
print(ans)
