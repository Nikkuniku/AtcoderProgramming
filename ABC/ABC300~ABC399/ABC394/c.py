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
i = 0
T = []
while i < len(R):
    if i < len(R) - 1:
        if R[i][0] == "W" and R[i + 1][0] == "A":
            T.append(("A", 1))
            T.append(("C", R[i][1]))
            T.append(("A", R[i + 1][1] - 1))
            i += 2
        else:
            T.append(R[i])
            i += 1
    else:
        T.append(R[i])
        i += 1
ans = []
for t, k in T:
    for _ in range(k):
        ans.append(t)
print(*ans, sep="")
