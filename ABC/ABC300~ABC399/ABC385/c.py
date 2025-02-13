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


from collections import defaultdict

N = int(input())
H = list(map(int, input().split()))
d = defaultdict(list)
for i, v in enumerate(H):
    d[v].append(i)
diffs = defaultdict(list)
for k in d.keys():
    for i in range(len(d[k]) - 1):
        diffs[k].append(d[k][i + 1] - d[k][i])
ans = 1
for k in d.keys():
    res = 1
    rle = RLE(diffs[k])
    for _, v in rle:
        res = max(res, v)
    ans = max(ans, res)
print(ans)
