from collections import defaultdict


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


d = defaultdict(list)
N = int(input())
A = list(map(int, input().split()))
C = RLE(A)
ans = 0
if len(C) == 1 and C[0][0] > 0:
    ans += 1

for i, v in enumerate(A):
    d[v].append(i)
B = sorted(list(d.items()), key=lambda x: x[0])
Lands = [0]+[1]*N+[0]
tmp = 1
for _, L in B:
    for i in L:
        i += 1
        if Lands[i-1] > 0 and Lands[i+1] > 0:
            tmp += 1
        elif Lands[i-1] == 0 and Lands[i+1] == 0:
            tmp -= 1
        Lands[i] = 0
    ans = max(ans, tmp)
print(ans)
