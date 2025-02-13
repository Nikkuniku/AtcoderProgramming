def RLE(S: list) -> list:
    """
    入力をランレングス圧縮したリストを返す.
    [(value1,length1),(value2,length2),...]

    Parameters
    ----------
    S:list

    Examples
    --------
    >>> RLE('aaabbc')
    [('a', 3), ('b', 2), ('c', 1)]
    """
    from itertools import groupby

    res = [(k, len(list(g))) for k, g in groupby(S)]
    return res


N = int(input())
S = input()
R = RLE(S)
ans = 1
MOD = 998244353
if "1" not in S:
    exit(print(0))
for i in range(len(R)):
    mid = R[i][0]
    if mid == "1":
        ans *= pow(2, R[i][1] - 1, MOD)
    if 0 <= i - 1 and i + 1 <= len(R) - 1:
        l = R[i - 1][0]
        r = R[i + 1][0]
        if l == r == "1" and mid == "0":
            ans *= R[i][1] + 2
    ans %= MOD
print(ans)
