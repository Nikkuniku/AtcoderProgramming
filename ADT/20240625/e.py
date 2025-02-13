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


from more_itertools import pairwise

N = int(input())
S = input()
rle = RLE(S)
ans = -1
for s, t in pairwise(rle):
    if s[0] == "o" and t[0] == "-":
        ans = max(ans, s[1])
    if s[0] == "-" and t[0] == "o":
        ans = max(ans, t[1])
print(ans)
