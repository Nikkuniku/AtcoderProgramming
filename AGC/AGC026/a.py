def RLE(S):
    from itertools import groupby
    res = [(k, len(list(g))) for k, g in groupby(S)]
    return res


N = int(input())
A = list(map(int, input().split()))
RL = RLE(A)
ans = 0
for k, l in RL:
    ans += l//2
print(ans)
