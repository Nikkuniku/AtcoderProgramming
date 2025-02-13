from collections import defaultdict


def RLE(S: list) -> list:
    """
    入力をランレングス圧縮したリストを返す.
    [(value1,length1),(value2,length2),...]

    Parameters
    -----------
    S:list

    Examples
    --------
    >>> RLE('aaabbc')
    [('a', 3), ('b', 2), ('c', 1)]
    """
    from more_itertools import run_length

    res = list(run_length.encode(S))
    return res


N = int(input())
S = input()
P = RLE(S)
d = defaultdict(int)
for s, e in P:
    d[s] = max(d[s], e)
ans = sum(d.values())
print(ans)
