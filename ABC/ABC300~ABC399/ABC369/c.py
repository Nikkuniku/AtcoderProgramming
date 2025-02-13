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
B = []
for i in range(N - 1):
    B.append(A[i + 1] - A[i])

r = RLE(B)
ans = N
for _, v in r:
    ans += v * (v + 1) // 2
print(ans)
