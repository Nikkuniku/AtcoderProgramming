from bisect import bisect_right


def RLE(S: list) -> list:
    '''
    入力をランレングス圧縮したリストを返す.
    [(value1,length1),(value2,length2),...]

    Parameters
    -----------
    S:list

    Examples
    --------
    >>> RLE('aaabbc')
    [('a', 3), ('b', 2), ('c', 1)]
    '''
    from itertools import groupby
    res = [(k, len(list(g))) for k, g in groupby(S)]
    return res


N = int(input())
A = list(map(int, input().split()))
B = [c for c, _ in RLE([0]+A+[0])]
M = len(B)
print(M)
print(B)
top = []
valley = []
C = []
for i in range(1, M-1):
    if B[i-1] < B[i] > B[i+1]:
        top.append(B[i])
    elif B[i-1] > B[i] < B[i+1]:
        valley.append(B[i])
for c in top:
    C.append(('t', c))
for c in valley:
    C.append(('v', c))
ans = 0
for b in valley:
    tmp = len(top)-bisect_right(top, b)
    ans = max(ans, tmp)
print(top)
print(valley)
print(ans)
