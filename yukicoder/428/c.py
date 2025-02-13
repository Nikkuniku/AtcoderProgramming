from itertools import accumulate

N, M, W = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]
B = list(map(int, input().split()))
C = list(map(int, input().split()))
cumA = list(accumulate(A, initial=0))
ans = 0
for i in range(1 << M):
    tmp = 0
    w = 0
    for j in range(M):
        if i & (1 << j):
            w += B[j]
            tmp += C[j]
    if w > W:
        continue
    tmp += cumA[min(W - w, N)]
    ans = max(ans, tmp)
print(ans)
