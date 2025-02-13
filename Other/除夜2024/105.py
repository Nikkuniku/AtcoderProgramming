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
cnt = 0
for i, v in enumerate(R):
    if v[0] == "1":
        cnt += 1
    if cnt == K:
        R[i - 1], R[i] = R[i], R[i - 1]
        break
ans = []
for k, v in R:
    for _ in range(v):
        ans.append(k)
print(*ans, sep="")
