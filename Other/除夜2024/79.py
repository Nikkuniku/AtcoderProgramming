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
A = list(map(int, input().split()))
B = [A[i] - A[i - 1] for i in range(1, N)]
R = RLE(B)
ans = N
for k, v in R:
    ans += (v + 1) * v // 2
print(ans)
