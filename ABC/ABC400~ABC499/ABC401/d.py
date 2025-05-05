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
S = list(input())
di = [-1, 1]
for i in range(N):
    if S[i] == "o":
        for d in di:
            ni = i + d
            if not (0 <= ni < N):
                continue
            if S[ni] == "?":
                S[ni] = "."
        if K > 0:
            K -= 1
R = RLE(S)
T = 0
i = 0
Odds = [False] * N
for s, v in R:
    if s == "?":
        if v % 2 != 0:
            for j in range(i, i + v):
                Odds[j] = True
        T += (v + 1) // 2
    i += v
if T == K:
    i = 0
    for s, v in R:
        if s == "?":
            if v % 2 != 0:
                for j in range(i, i + v, 2):
                    S[j] = "o"
        i += v
    for i in range(N):
        if S[i] == "o":
            for d in di:
                ni = i + d
                if not (0 <= ni < N):
                    continue
                if S[ni] == "?":
                    S[ni] = "."
if K == 0:
    for i in range(N):
        if S[i] == "?":
            S[i] = "."
print(*S, sep="")
