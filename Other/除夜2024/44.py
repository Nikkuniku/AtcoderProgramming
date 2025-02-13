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


N, K = map(int, input().split())
S = input()
R = RLE(S)
ans = 0
for s, v in R:
    if s == "O":
        ans += v // K
print(ans)
