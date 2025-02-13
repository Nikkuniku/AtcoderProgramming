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
rle = RLE(S)
ans = "No"
if len(rle) == 3:
    if rle[0][0] == "A" and rle[1][0] == "B" and rle[2][0] == "C":
        ans = "Yes"
elif len(rle) == 2:
    if (
        (rle[0][0] == "A" and rle[1][0] == "B")
        or (rle[0][0] == "B" and rle[1][0] == "C")
        or (rle[0][0] == "A" and rle[1][0] == "C")
    ):
        ans = "Yes"
elif len(rle) == 1:
    ans = "Yes"
print(ans)
