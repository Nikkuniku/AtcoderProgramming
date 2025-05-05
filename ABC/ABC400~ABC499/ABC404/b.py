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
T = [list(input()) for _ in range(N)]
ans = 1 << 60
for i in range(4):
    temp = i + 1
    if i == 3:
        temp = 0
    S = matrix_rotate90degree_toright(S)
    for a in range(N):
        for b in range(N):
            if S[a][b] != T[a][b]:
                temp += 1
    ans = min(ans, temp)
print(ans)
