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


N, D = map(int, input().split())
tmp = [0] * D
for _ in range(N):
    S = list(input())
    for i in range(D):
        if S[i] == "o":
            tmp[i] += 1
S = RLE(tmp)
ans = 0
for v, c in S:
    if v == N:
        ans = max(ans, c)
print(ans)
