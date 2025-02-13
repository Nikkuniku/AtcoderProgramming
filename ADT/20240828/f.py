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


S = input()
T = input()
RLE_S = RLE(S)
RLE_T = RLE(T)
ans = "No"
if len(RLE_S) == len(RLE_T):
    isOK = True
    for i in range(len(RLE_S)):
        s, p = RLE_S[i]
        t, q = RLE_T[i]
        if not (s == t and ((p == 1 and q == 1) or (2 <= p <= q))):
            isOK = False
            break
    if isOK:
        ans = "Yes"
print(ans)
