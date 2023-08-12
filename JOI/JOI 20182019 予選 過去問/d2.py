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


d = defaultdict(int)
N = int(input())
A = list(map(int, input().split()))
S = sorted(list(set(A+[0])))
for i in range(len(S)):
    d[S[i]] = i
A = [d[a] for a in A]
B = [c for c, _ in RLE([0]+A+[0])]
M = len(B)
pre = -1
up = True
C = []
for i in range(M):
    if up:
        if pre > B[i]:
            C.append(pre)
            up = False
    else:
        if pre < B[i]:
            C.append(pre)
            up = True
    pre = B[i]
ranges = []
for i in range(len(C)):
    if i == 0 or i == len(C)-1:
        ranges.append((0, C[i]))
    else:
        if C[i-1] > C[i] < C[i+1]:
            ranges.append((C[i], min(C[i-1], C[i+1])))
imos = [0]*(max(A)+3)
for p, q in ranges:
    imos[p] += 1
    imos[q] -= 1
for i in range(len(imos)-1):
    imos[i+1] += imos[i]
print(max(imos)-1)
