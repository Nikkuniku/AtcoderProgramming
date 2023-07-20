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


print(RLE('aabbbc'))
print(RLE([1, 1, 2, 3, 4, 4, 5]))
