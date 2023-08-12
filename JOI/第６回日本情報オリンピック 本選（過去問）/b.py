from itertools import groupby
N, K = map(int, input().split())
A = [0]*N
joker = False
for _ in range(K):
    S = int(input())
    if S == 0:
        joker = True
        continue
    A[S-1] = 1
gr = groupby(A)
B = [(k, len(list(v))) for k, v in gr]
ans = 0
for i in range(len(B)):
    k, v = B[i]
    if k == 1:
        ans = max(ans, v)
        continue
    if joker:
        tmp = []
        for j in [-1, 1]:
            if 0 <= i+j < len(B):
                tmp.append(B[i+j][1])
        if v == 1:
            ans = max(ans, sum(tmp)+1)
        else:
            ans = max(ans, max(tmp)+1)

print(ans)
