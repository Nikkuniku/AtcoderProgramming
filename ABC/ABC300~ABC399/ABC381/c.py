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
R = RLE(S)
ans = 1
for i, v in enumerate(R):
    if v[0] == "/" and v[1] == 1:
        if 0 < i < len(R) - 1:
            a, b = R[i - 1]
            c, d = R[i + 1]
            if a == "1" and c == "2":
                T = min(b, d)
                ans = max(ans, 2 * T + 1)
print(ans)
