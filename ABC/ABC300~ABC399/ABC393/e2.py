N, K = map(int, input().split())
A = list(map(int, input().split()))
L = 10**6
M = [[] for _ in range(L + 1)]
for i, a in enumerate(A):
    M[a].append(i)
ans = [1] * N
for g in range(L, 1, -1):
    cnt = 0
    j = g
    while j <= L:
        cnt += len(M[j])
        j += g
    if cnt < K:
        continue
    j = g
    while j <= L:
        for i in M[j]:
            if ans[i] == 1:
                ans[i] = g
        j += g
print(*ans, sep="\n")
