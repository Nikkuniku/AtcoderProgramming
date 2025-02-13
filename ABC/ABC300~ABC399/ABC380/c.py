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
i = -1
cnt = 0
for k, v in R:
    i += 1
    if k == "1":
        cnt += 1
    if cnt == K:
        break
R[i - 1], R[i] = R[i], R[i - 1]
ans = []
for i, v in R:
    for _ in range(v):
        ans.append(i)
print(*ans, sep="")
