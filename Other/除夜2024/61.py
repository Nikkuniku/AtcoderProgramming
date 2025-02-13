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
R = RLE(S)
ans = "No"
if len(R) == 1:
    ans = "Yes"
elif len(R) == 2:
    if (
        (R[0][0] == "A" and R[1][0] == "B")
        or (R[0][0] == "A" and R[1][0] == "C")
        or (R[0][0] == "B" and R[1][0] == "C")
    ):
        ans = "Yes"
elif len(R) == 3:
    if R[0][0] == "A" and R[1][0] == "B" and R[2][0] == "C":
        ans = "Yes"
print(ans)
