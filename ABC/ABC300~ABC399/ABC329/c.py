from string import ascii_lowercase


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


from collections import defaultdict

N = int(input())
S = input()
d = defaultdict(int)
R = RLE(S)
for s, v in R:
    d[s] = max(d[s], v)
ans = 0
for k, v in d.items():
    ans += v
print(ans)
