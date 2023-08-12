def RLE(S: list) -> list:
    '''
    入力をランレングス圧縮したリストを返す.
    [(value1,length1),(value2,length2),...]

    Parameters
    -----------
    S:list

    Examples
    --------
    >>> RLE('aaabbc')
    [('a', 3), ('b', 2), ('c', 1)]
    '''
    from itertools import groupby
    res = [(k, len(list(g))) for k, g in groupby(S)]
    return res


N, D = map(int, input().split())
S = [input() for _ in range(N)]
T = []
for i in range(D):
    res = 0
    for j in range(N):
        if S[j][i] == 'x':
            res = 1
    T.append(res)
P = RLE(T)
ans = 0
for k, j in P:
    if k == 0:
        ans = max(ans, j)
print(ans)
