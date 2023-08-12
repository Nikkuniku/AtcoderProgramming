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


N = int(input())
A, B = map(int, input().split())
P = []
for _ in range(N):
    p, q, r, s = map(int, input().split())
    for i in range(p, r+1):
        for j in range(q, s+1):
            P.append((i, j))
P.sort()
Q = RLE(P)
ans = max([c for _, c in Q])
square = 0
for _, c in Q:
    square += c == ans
print(ans)
print(square)
