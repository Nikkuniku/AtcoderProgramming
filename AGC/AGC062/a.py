def RLE(S: list) -> list:
    '''
    入力をランレングス圧縮したリストを返す.
    [(value1,length1),(value2,length2),...]

    Parameters
    ----------
    S:list

    Examples
    --------
    >>> RLE('aaabbc')
    [('a', 3), ('b', 2), ('c', 1)]
    '''
    from itertools import groupby
    res = [(k, len(list(g))) for k, g in groupby(S)]
    return res


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    R = RLE(S)
    res = 'A'
    if (len(R) == 2 and R[0][0] == 'A' and R[1][0] == 'B') or (len(R) == 1 and R[0][0] == 'B'):
        res = 'B'
    ans.append(res)
print(*ans, sep="\n")
